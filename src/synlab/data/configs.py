# defines the data-related configuration objects.
# later edit paths and column names to match the actual files

# src/synlab/data/configs.py

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from synlab.utils.paths import get_project_root

# Single source of truth for paths
PROJECT_ROOT: Path = get_project_root()


# -------------------------------------------------------------------
# RVU (travel survey) config
# -------------------------------------------------------------------


@dataclass
class RVUSampleConfig:
    """
    Configuration for the RVU (travel survey) microdata.

    raw_path:
        SPSS .sav file with individual/household travel survey responses.
    processed_path:
        Parquet file produced by the RVU pipeline and consumed by methods.
    """

    # Paths
    raw_path: Path = (
        PROJECT_ROOT
        / "data"
        / "raw"
        / "population"
        / "rvu"
        / "Filemail.com - RVU 2025"
        / "rvu_sampleNasjonal_RVU_PERSON_Nov26_0901.sav"
    )
    processed_path: Path = PROJECT_ROOT / "data" / "processed" / "rvu_sample.parquet"

    # Column names in the raw .sav file
    raw_bsu_col: str = "grunnkrets"  # BSU / spatial unit
    weight_col: Optional[str] = None  # e.g. "vekt"

    # Optional map from raw -> internal variable names
    # e.g. {"kjonn": "sex", "aldergr": "age_group"}
    variable_name_map: Optional[Dict[str, str]] = None


# -------------------------------------------------------------------
# Population marginals config
# -------------------------------------------------------------------


@dataclass
class MarginalSourceConfig:
    """
    Configuration for a single marginal table (one DBF file).

    Example: BSU x age, or BSU x gender, etc.
    """

    name: str  # logical name: "age", "gender", "education", ...
    raw_path: Path

    # Column names in the raw DBF file
    raw_bsu_col: str = "grunnkrets"  # spatial unit in this DBF
    category_col: str = "category"  # column with the category label
    count_col: str = "count"  # column with the count

    # Optional: if needed later for more complex shapes (wide -> long), we can extend this


@dataclass
class PopulationMarginalsConfig:
    """
    Configuration for all population marginal tables used for synthesis.

    sources:
        List of marginal sources (age, gender, education, income, ...).
    processed_path:
        Single Parquet file combining all marginals in long format with columns:
            ['bsu_id', 'variable', 'category', 'count']
    """

    sources: List[MarginalSourceConfig] = field(default_factory=list)
    processed_path: Path = PROJECT_ROOT / "data" / "processed" / "population_marginals.parquet"


# -------------------------------------------------------------------
# GeoSTAD (Business registry) config
# -------------------------------------------------------------------


@dataclass
class GeoSTADConfig:
    """
    Configuration for the GeoSTAD business registry dataset.

    raw_path:
        SPSS .sav file with geocoded business locations.
    processed_path:
        Parquet file with cleaned and preprocessed business data.
    """

    # Paths
    raw_path: Path = PROJECT_ROOT / "data" / "raw" / "population" / "geostad" / "VoF2025_geokodet.SAV"
    processed_path: Path = PROJECT_ROOT / "data" / "processed" / "population" / "geostad_businesses.parquet"

    # Processing options
    filter_geocoded: bool = True  # Only include businesses with coordinates
    remove_duplicates: bool = True  # Remove duplicate rows

    # Feature columns to use for synthesis
    # Only include independent features (grk2025 and fpnr2025 are derived from X/Y)
    feature_columns: List[str] = field(
        default_factory=lambda: [
            "SN2025",  # Industry code (independent)
            "orgf2025",  # Organization type (independent)
            "X_2025",  # X-coordinate (location)
            "Y_2025",  # Y-coordinate (location)
        ]
    )

    # Identifier columns (loaded but not used for synthesis)
    # These are quasi-unique values that don't provide modeling value
    identifier_columns: List[str] = field(
        default_factory=lambda: [
            "orgn2025",  # Organization number (21% unique in sample)
            "navn2025",  # Business name (21% unique in sample)
        ]
    )

    # Derived columns to reconstruct after synthesis
    # Format: {derived_column: source_column} - derived column is reconstructed from source
    # Note: grk2025 and fpnr2025 require spatial lookups from X/Y coordinates
    derived_columns: Dict[str, str] = field(
        default_factory=lambda: {
            "fpst2025": "fpnr2025",  # Postal area name from postal code
            # Note: grk2025 and fpnr2025 need spatial reconstruction from X_2025/Y_2025
            # This requires spatial join with reference geometries (not simple mapping)
        }
    )

    # Computed properties for column types (no duplication with feature_columns)
    @property
    def coordinate_columns(self) -> List[str]:
        """Spatial coordinate columns used for filtering and metadata."""
        return ["X_2025", "Y_2025"]

    @property
    def continuous_columns(self) -> List[str]:
        """Feature columns with continuous (numeric) values."""
        return [col for col in self.feature_columns if col in self.coordinate_columns]

    @property
    def categorical_columns(self) -> List[str]:
        """Feature columns with categorical (discrete) values."""
        return [col for col in self.feature_columns if col not in self.continuous_columns]

    @property
    def spatial_unit_column(self) -> str:
        """Column name for spatial aggregation units (BSU/grid cells)."""
        return "grk2025"

    def __post_init__(self):
        """Validate configuration after initialization."""
        # Validate paths exist
        if not self.raw_path.exists():
            raise FileNotFoundError(
                f"Raw data file not found: {self.raw_path}\n"
                f"Please ensure the GeoSTAD data file exists at the specified location."
            )

        # Validate no overlap between feature and identifier columns
        feature_set = set(self.feature_columns)
        identifier_set = set(self.identifier_columns)
        overlap = feature_set & identifier_set
        if overlap:
            raise ValueError(
                f"Columns cannot be both features and identifiers: {overlap}\n"
                f"Please remove these from either feature_columns or identifier_columns."
            )

        # Validate coordinate columns are in features
        coord_set = set(self.coordinate_columns)
        missing_coords = coord_set - feature_set
        if missing_coords:
            raise ValueError(
                f"Coordinate columns {missing_coords} not found in feature_columns.\n"
                f"Coordinate columns must be included in features for synthesis."
            )

        # Note: derived_columns and spatial_unit_column don't need to be in feature_columns
        # They can be reconstructed after synthesis using spatial lookups or mappings

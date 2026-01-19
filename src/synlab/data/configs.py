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
    raw_path: Path = PROJECT_ROOT / "data" / "raw" / "population" / "rvu" / "Filemail.com - RVU 2025" / "rvu_sampleNasjonal_RVU_PERSON_Nov26_0901.sav"
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
    category_col: str = "category"   # column with the category label
    count_col: str = "count"         # column with the count

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

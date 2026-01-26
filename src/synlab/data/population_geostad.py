"""
Data loader for GeoSTAD (Norwegian business registry) dataset.

Provides functions to load and preprocess the VoF2025_geokodet.SAV file
containing geocoded business locations with organization info.

QUICK REFERENCE:
- config.feature_columns → columns used for synthesis (e.g., ["SN2025", "X_2025", ...])
- config.derived_columns → columns reconstructed after synthesis (e.g., {"fpst2025": "fpnr2025"})
- config.coordinate_columns → spatial coordinates (["X_2025", "Y_2025"])
- config.continuous_columns → numeric features (coordinates)
- config.categorical_columns → discrete features (industry, postal code, etc.)

MAIN FUNCTIONS:
- load_geostad(config) → loads raw data, returns (df, domain)
- prepare_for_synthesis(df, config) → extracts feature columns only

POST-SYNTHESIS RECONSTRUCTION (use generic functions from synlab.utils.postprocessing):
- create_derived_mappings(config) → builds {derived_col: {source_val: derived_val}}
- reconstruct_derived_columns(df, mappings, config) → adds derived columns back

Example workflow:
    config = GeoSTADConfig()
    df, domain = load_geostad(config)
    df_features = prepare_for_synthesis(df, config)
    # ... run synthesis to get df_synthetic ...
    mappings = create_derived_mappings(config)  # Get postal code->name mapping
    df_final = reconstruct_derived_columns(df_synthetic, mappings, config)
"""

from typing import Any, Dict, Optional, Tuple

import pandas as pd
import pyreadstat

from synlab.data.configs import GeoSTADConfig


def load_geostad(config: Optional[GeoSTADConfig] = None) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Load the GeoSTAD business registry dataset using configuration.

    Parameters
    ----------
    config : GeoSTADConfig, optional
        Configuration object with paths and processing options.
        If None, uses default GeoSTADConfig().

    Returns
    -------
    df : pd.DataFrame
        Cleaned GeoSTAD business dataset.
    domain : dict
        Domain metadata including column types, coordinate ranges, and category info.
    """
    # Use default config if none provided
    if config is None:
        config = GeoSTADConfig()

    # Validate file exists (config validation should catch this, but double-check)
    if not config.raw_path.exists():
        raise FileNotFoundError(
            f"GeoSTAD data file not found: {config.raw_path}\n"
            f"Please check that the file exists and the path is correct."
        )

    # Load SPSS file with error handling
    try:
        df, meta = pyreadstat.read_sav(str(config.raw_path))
    except Exception as e:
        raise ValueError(
            f"Failed to load SPSS file '{config.raw_path.name}': {str(e)}\n"
            f"The file may be corrupted or in an unsupported format."
        ) from e

    # Validate that all required columns exist in the loaded data
    columns_to_load = config.feature_columns + config.identifier_columns
    available_columns = set(df.columns)
    missing_columns = set(columns_to_load) - available_columns

    if missing_columns:
        raise ValueError(
            f"Missing expected columns in data file: {missing_columns}\n"
            f"Available columns: {sorted(available_columns)}\n"
            f"Please check the config matches the actual data schema."
        )

    # Select columns: features + identifiers
    df = df[columns_to_load].copy()

    # Filter for geocoded businesses if requested
    if config.filter_geocoded:
        initial_count = len(df)
        df = df.dropna(subset=config.coordinate_columns)
        print(f"Filtered to geocoded businesses: {len(df):,} / {initial_count:,} rows")

    # Remove duplicates if requested
    if config.remove_duplicates:
        initial_count = len(df)
        df = df.drop_duplicates()
        removed = initial_count - len(df)
        if removed > 0:
            print(f"Removed {removed:,} duplicate rows: {len(df):,} rows remaining")

    # Build domain metadata
    domain = _build_domain_metadata(df, config)

    return df, domain


def _build_domain_metadata(df: pd.DataFrame, config: GeoSTADConfig) -> Dict[str, Any]:
    """
    Build domain metadata for GeoSTAD dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned GeoSTAD dataframe.
    config : GeoSTADConfig
        Configuration with column type specifications.

    Returns
    -------
    domain : dict
        Dictionary containing:
        - column_types: mapping of column names to types (continuous, categorical)
        - coordinate_bounds: min/max for X and Y coordinates
        - categorical_info: cardinality and top categories for each categorical column
    """
    domain = {"column_types": {}, "coordinate_bounds": {}, "categorical_info": {}, "spatial_info": {}}

    # Identify column types from config (no hardcoding!)
    for col in df.columns:
        if col in config.continuous_columns:
            domain["column_types"][col] = "continuous"
        elif col in config.categorical_columns:
            domain["column_types"][col] = "categorical"
        elif col in config.identifier_columns:
            domain["column_types"][col] = "identifier"

    # Store coordinate bounds using config
    if all(col in df.columns for col in config.coordinate_columns):
        x_col, y_col = config.coordinate_columns
        domain["coordinate_bounds"] = {
            "X_min": float(df[x_col].min()),
            "X_max": float(df[x_col].max()),
            "Y_min": float(df[y_col].min()),
            "Y_max": float(df[y_col].max()),
        }

    # Store categorical information using config
    for col in config.categorical_columns:
        if col in df.columns:
            value_counts = df[col].value_counts()
            domain["categorical_info"][col] = {
                "cardinality": int(df[col].nunique()),
                "top_10": value_counts.head(10).to_dict(),
                "missing_count": int(df[col].isna().sum()),
            }

    # Store spatial information using config
    spatial_col = config.spatial_unit_column
    if spatial_col in df.columns:
        domain["spatial_info"]["n_spatial_units"] = int(df[spatial_col].nunique())
        domain["spatial_info"]["avg_businesses_per_unit"] = float(df.groupby(spatial_col).size().mean())

    return domain


def prepare_for_synthesis(
    df: pd.DataFrame, config: Optional[GeoSTADConfig] = None, sample_size: Optional[int] = None, random_state: int = 42
) -> pd.DataFrame:
    """
    Prepare GeoSTAD data for synthetic generation.

    Parameters
    ----------
    df : pd.DataFrame
        Raw GeoSTAD dataframe.
    config : GeoSTADConfig, optional
        Configuration object specifying feature columns. If None, uses default.
    sample_size : int, optional
        Number of records to sample. If None, uses all data.
    random_state : int, default=42
        Random seed for reproducibility.

    Returns
    -------
    pd.DataFrame
        Prepared dataframe with only feature columns.
    """
    # Use default config if none provided
    if config is None:
        config = GeoSTADConfig()

    # Validate that feature columns exist in dataframe
    missing_features = set(config.feature_columns) - set(df.columns)
    if missing_features:
        raise ValueError(
            f"Missing feature columns in dataframe: {missing_features}\n"
            f"Available columns: {sorted(df.columns)}\n"
            f"Ensure load_geostad() was called first or config matches your data."
        )

    # Select feature columns from config
    df_features = df[config.feature_columns].copy()

    # Validate sample size
    if sample_size is not None:
        if sample_size <= 0:
            raise ValueError(f"sample_size must be positive, got {sample_size}")
        if sample_size > len(df_features):
            raise ValueError(
                f"sample_size ({sample_size:,}) exceeds available data ({len(df_features):,})\n"
                f"Use a smaller sample_size or set it to None to use all data."
            )

    # Sample if requested
    if sample_size is not None and sample_size < len(df_features):
        df_features = df_features.sample(n=sample_size, random_state=random_state)
        print(f"Sampled {sample_size:,} records from {len(df):,}")

    return df_features

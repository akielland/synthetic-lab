"""
Generic utilities for reconstructing derived columns after synthesis.

These functions work with any dataset config that specifies derived_columns,
making them reusable across different datasets (GeoSTAD, RVU, TraMOD, etc.).
"""

from typing import Any, Dict

import pandas as pd
import pyreadstat


def create_derived_mappings(config: Any) -> Dict[str, Dict[str, str]]:
    """
    Create mappings for all derived columns specified in config.

    Uses config.derived_columns to determine which columns need mapping.
    For each derived column, creates a mapping from source to derived values.

    This is a generic function that works with any config class that has:
    - derived_columns: Dict[str, str] (derived_col -> source_col)
    - raw_path: Path (path to raw data file)

    Parameters
    ----------
    config : Any config object
        Configuration with derived_columns and raw_path attributes.
        Works with GeoSTADConfig, RVUSampleConfig, etc.

    Returns
    -------
    dict of dict
        Nested mapping: {derived_col: {source_value: derived_value}}
        Example: {"fpst2025": {"0177": "OSLO", "5089": "BERGEN"}}
    """
    if not hasattr(config, "derived_columns") or not config.derived_columns:
        print("No derived columns specified in config")
        return {}

    if not hasattr(config, "raw_path"):
        raise AttributeError("Config must have 'raw_path' attribute")

    # Collect all columns needed for mappings
    columns_needed = set()
    for derived_col, source_col in config.derived_columns.items():
        columns_needed.add(source_col)
        columns_needed.add(derived_col)

    # Load only required columns from raw data
    df, meta = pyreadstat.read_sav(str(config.raw_path), usecols=list(columns_needed))

    # Create mapping for each derived column
    mappings = {}
    for derived_col, source_col in config.derived_columns.items():
        # Get unique source-derived pairs, excluding empty values
        mapping_df = df[[source_col, derived_col]].dropna().drop_duplicates()

        # Convert to dictionary
        mapping = dict(zip(mapping_df[source_col], mapping_df[derived_col], strict=True))
        mappings[derived_col] = mapping

        print(f"Created mapping for {derived_col} from {source_col}: {len(mapping)} unique values")

    return mappings


def reconstruct_derived_columns(
    df_synthetic: pd.DataFrame,
    mappings: Dict[str, Dict[str, str]],
    config: Any,
) -> pd.DataFrame:
    """
    Reconstruct all derived columns in synthetic data using mappings from real data.

    Uses config.derived_columns to determine which columns to reconstruct and from
    which source columns. This makes synthetic data more readable and comparable
    to the original dataset.

    This is a generic function that works with any config class that has:
    - derived_columns: Dict[str, str] (derived_col -> source_col)

    Parameters
    ----------
    df_synthetic : pd.DataFrame
        Synthetic data with source columns but no derived columns.
    mappings : dict of dict
        Nested mapping created by create_derived_mappings().
        Format: {derived_col: {source_value: derived_value}}
    config : Any config object
        Configuration with derived_columns attribute.
        Works with GeoSTADConfig, RVUSampleConfig, etc.

    Returns
    -------
    pd.DataFrame
        Synthetic data with all derived columns reconstructed.
    """
    if not hasattr(config, "derived_columns") or not config.derived_columns:
        print("No derived columns specified in config")
        return df_synthetic

    df_result = df_synthetic.copy()

    # Reconstruct each derived column
    for derived_col, source_col in config.derived_columns.items():
        if source_col not in df_result.columns:
            print(f"Warning: Source column '{source_col}' not found, skipping {derived_col}")
            continue

        if derived_col not in mappings:
            print(f"Warning: No mapping for '{derived_col}', skipping")
            continue

        # Apply mapping
        df_result[derived_col] = df_result[source_col].map(mappings[derived_col])

        # Report on missing mappings
        missing_count = df_result[derived_col].isna().sum()
        if missing_count > 0:
            missing_vals = df_result[df_result[derived_col].isna()][source_col].unique()
            print(f"Warning: {missing_count} records have unmapped {source_col} values:")
            print(f"  Unmapped: {missing_vals[:10]}")  # Show first 10
        else:
            print(f"✓ Reconstructed {derived_col} from {source_col} for all {len(df_result):,} records")

    return df_result

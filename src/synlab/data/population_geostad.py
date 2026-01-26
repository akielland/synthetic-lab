"""
Data loader for GeoSTAD (Norwegian business registry) dataset.

Provides functions to load and preprocess the VoF2025_geokodet.SAV file
containing geocoded business locations with organization info.
"""

from pathlib import Path
from typing import Any, Dict, List, Tuple

import pandas as pd
import pyreadstat

from synlab.utils.paths import get_project_root


def load_geostad(
    columns: List[str] = None, filter_geocoded: bool = True, remove_duplicates: bool = True
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Load the GeoSTAD business registry dataset.

    Parameters
    ----------
    columns : List[str], optional
        List of columns to load. If None, loads a default set of relevant columns.
    filter_geocoded : bool, default=True
        If True, only include businesses with valid X/Y coordinates.
    remove_duplicates : bool, default=True
        If True, remove duplicate rows after filtering.

    Returns
    -------
    df : pd.DataFrame
        Cleaned GeoSTAD business dataset.
    domain : dict
        Domain metadata including column types, coordinate ranges, and category info.
    """
    root = get_project_root()
    geostad_path = root / "data" / "raw" / "population" / "geostad" / "VoF2025_geokodet.SAV"

    # Load SPSS file
    df, meta = pyreadstat.read_sav(str(geostad_path))

    # Define default columns of interest
    if columns is None:
        columns = [
            "orgn2025",  # Organization number
            "navn2025",  # Business name
            "SN2025",  # Industry code / type of business
            "orgf2025",  # Organization type
            "fpst2025",  # Postal area
            "fpnr2025",  # Postal code
            "grk2025",  # Grid cell number (grunnkrets/BSU sone)
            "X_2025",  # X-coordinate (UTM coordinate system)
            "Y_2025",  # Y-coordinate (UTM coordinate system)
        ]

    # Select columns
    df = df[columns].copy()  # .copy to avoid SettingWithCopyWarning

    # Filter for geocoded businesses if requested
    if filter_geocoded:
        initial_count = len(df)
        df = df.dropna(subset=["X_2025", "Y_2025"])
        print(f"Filtered to geocoded businesses: {len(df):,} / {initial_count:,} rows")

    # Remove duplicates if requested
    if remove_duplicates:
        initial_count = len(df)
        df = df.drop_duplicates()
        removed = initial_count - len(df)
        if removed > 0:
            print(f"Removed {removed:,} duplicate rows: {len(df):,} rows remaining")

    # Build domain metadata
    domain = _build_domain_metadata(df)

    return df, domain


def _build_domain_metadata(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Build domain metadata for GeoSTAD dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned GeoSTAD dataframe.

    Returns
    -------
    domain : dict
        Dictionary containing:
        - column_types: mapping of column names to types (continuous, categorical)
        - coordinate_bounds: min/max for X and Y coordinates
        - categorical_info: cardinality and top categories for each categorical column
    """
    domain = {"column_types": {}, "coordinate_bounds": {}, "categorical_info": {}, "spatial_info": {}}

    # Identify column types
    continuous_cols = ["X_2025", "Y_2025"]
    categorical_cols = ["SN2025", "orgf2025", "fpst2025", "fpnr2025", "grk2025"]
    identifier_cols = ["orgn2025", "navn2025"]

    for col in df.columns:
        if col in continuous_cols:
            domain["column_types"][col] = "continuous"
        elif col in categorical_cols:
            domain["column_types"][col] = "categorical"
        elif col in identifier_cols:
            domain["column_types"][col] = "identifier"

    # Store coordinate bounds
    if "X_2025" in df.columns and "Y_2025" in df.columns:
        domain["coordinate_bounds"] = {
            "X_min": float(df["X_2025"].min()),
            "X_max": float(df["X_2025"].max()),
            "Y_min": float(df["Y_2025"].min()),
            "Y_max": float(df["Y_2025"].max()),
        }

    # Store categorical information
    for col in categorical_cols:
        if col in df.columns:
            value_counts = df[col].value_counts()
            domain["categorical_info"][col] = {
                "cardinality": int(df[col].nunique()),
                "top_10": value_counts.head(10).to_dict(),
                "missing_count": int(df[col].isna().sum()),
            }

    # Store spatial information
    if "grk2025" in df.columns:
        domain["spatial_info"]["n_spatial_units"] = int(df["grk2025"].nunique())
        domain["spatial_info"]["avg_businesses_per_unit"] = float(df.groupby("grk2025").size().mean())

    return domain


def get_feature_columns(exclude_identifiers: bool = True, exclude_names: bool = True) -> List[str]:
    """
    Get list of feature columns for modeling.

    Parameters
    ----------
    exclude_identifiers : bool, default=True
        Exclude organization numbers and postal area names.
    exclude_names : bool, default=True
        Exclude business names.

    Returns
    -------
    List[str]
        List of column names to use as features.
    """
    all_columns = ["orgn2025", "navn2025", "SN2025", "orgf2025", "fpst2025", "fpnr2025", "grk2025", "X_2025", "Y_2025"]

    feature_cols = all_columns.copy()

    if exclude_identifiers:
        feature_cols.remove("orgn2025")
        feature_cols.remove("fpst2025")

    if exclude_names:
        feature_cols.remove("navn2025")

    return feature_cols


def prepare_for_synthesis(df: pd.DataFrame, sample_size: int = None, random_state: int = 42) -> pd.DataFrame:
    """
    Prepare GeoSTAD data for synthetic generation.

    Parameters
    ----------
    df : pd.DataFrame
        Raw GeoSTAD dataframe.
    sample_size : int, optional
        Number of records to sample. If None, uses all data.
    random_state : int, default=42
        Random seed for reproducibility.

    Returns
    -------
    pd.DataFrame
        Prepared dataframe with only feature columns.
    """
    # Get feature columns
    feature_cols = get_feature_columns()
    df_features = df[feature_cols].copy()

    # Sample if requested
    if sample_size is not None and sample_size < len(df_features):
        df_features = df_features.sample(n=sample_size, random_state=random_state)
        print(f"Sampled {sample_size:,} records from {len(df):,}")

    return df_features

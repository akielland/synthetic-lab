#  quick-and-dirty sanity checks (marginals, means, variances…)


from __future__ import annotations

from typing import Dict, List, Optional, Any

import numpy as np
import pandas as pd
from pandas.api.types import (
    is_numeric_dtype,
    is_categorical_dtype,
    is_object_dtype,
    is_bool_dtype,
)


def _get_common_columns(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    columns: Optional[List[str]] = None,
) -> List[str]:
    """
    Return the list of columns to compare, ensuring they exist in both DataFrames.
    """
    if columns is None:
        columns = [c for c in real_df.columns if c in synth_df.columns]

    missing_real = [c for c in columns if c not in real_df.columns]
    missing_synth = [c for c in columns if c not in synth_df.columns]

    if missing_real or missing_synth:
        msg_parts = []
        if missing_real:
            msg_parts.append(f"Missing in real_df: {missing_real}")
        if missing_synth:
            msg_parts.append(f"Missing in synth_df: {missing_synth}")
        raise ValueError("Column mismatch between real and synthetic data. " + "; ".join(msg_parts))

    return columns


def _infer_col_type(series: pd.Series, max_categories: int = 20) -> str:
    """
    Simple heuristic to decide if a column is numeric or categorical.
    Returns: 'numeric', 'categorical', or 'other'
    """
    if is_bool_dtype(series):
        return "categorical"

    if is_numeric_dtype(series):
        return "numeric"

    if is_categorical_dtype(series) or is_object_dtype(series):
        # If it has few distinct values, we treat it as categorical.
        nunique = series.nunique(dropna=True)
        if nunique <= max_categories:
            return "categorical"
        return "other"

    return "other"


# ----------------------------------------------------------------------
# 1) Missingness comparison
# ----------------------------------------------------------------------


def compare_missingness(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    columns: Optional[List[str]] = None,
) -> pd.DataFrame:
    """
    Compare fraction of missing values per column.

    Returns a DataFrame indexed by column with:
        real_missing, synthetic_missing, abs_diff
    """
    cols = _get_common_columns(real_df, synth_df, columns)
    rows = []

    for col in cols:
        real_missing = real_df[col].isna().mean()
        synth_missing = synth_df[col].isna().mean()
        rows.append(
            {
                "column": col,
                "real_missing": real_missing,
                "synthetic_missing": synth_missing,
                "abs_diff": abs(real_missing - synth_missing),
            }
        )

    result = pd.DataFrame(rows).set_index("column").sort_values("abs_diff", ascending=False)
    return result


# ----------------------------------------------------------------------
# 2) Basic numeric stats
# ----------------------------------------------------------------------


def compare_basic_stats(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    columns: Optional[List[str]] = None,
) -> pd.DataFrame:
    """
    Compare basic statistics for numeric columns:
        mean, std, min, max, p25, p50, p75

    Returns a DataFrame indexed by column, with columns like:
        real_mean, synthetic_mean, diff_mean, ...
    """
    cols = _get_common_columns(real_df, synth_df, columns)
    rows = []

    for col in cols:
        real_col = real_df[col]
        synth_col = synth_df[col]

        # Only compare if both are numeric
        if not (is_numeric_dtype(real_col) and is_numeric_dtype(synth_col)):
            continue

        real_desc = {
            "mean": real_col.mean(),
            "std": real_col.std(),
            "min": real_col.min(),
            "max": real_col.max(),
            "p25": real_col.quantile(0.25),
            "p50": real_col.quantile(0.50),
            "p75": real_col.quantile(0.75),
        }

        synth_desc = {
            "mean": synth_col.mean(),
            "std": synth_col.std(),
            "min": synth_col.min(),
            "max": synth_col.max(),
            "p25": synth_col.quantile(0.25),
            "p50": synth_col.quantile(0.50),
            "p75": synth_col.quantile(0.75),
        }

        row = {"column": col}
        for key in real_desc.keys():
            row[f"real_{key}"] = real_desc[key]
            row[f"synthetic_{key}"] = synth_desc[key]
            row[f"diff_{key}"] = synth_desc[key] - real_desc[key]

        rows.append(row)

    result = pd.DataFrame(rows).set_index("column")
    return result.sort_index()


# ----------------------------------------------------------------------
# 3) Categorical frequencies
# ----------------------------------------------------------------------


def compare_category_frequencies(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    normalize: bool = True,
    max_categories: int = 20,
) -> Dict[str, pd.DataFrame]:
    """
    Compare category distributions for categorical columns.

    Returns a dict: {column_name: DataFrame}

    Each DataFrame is indexed by category, with columns:
        real, synthetic, abs_diff
    and sorted by abs_diff descending, truncated to max_categories rows.
    """
    cols = _get_common_columns(real_df, synth_df, columns)
    results: Dict[str, pd.DataFrame] = {}

    for col in cols:
        real_col = real_df[col]
        synth_col = synth_df[col]

        col_type = _infer_col_type(real_col, max_categories=max_categories)
        if col_type != "categorical":
            continue

        real_counts = real_col.value_counts(dropna=False, normalize=normalize)
        synth_counts = synth_col.value_counts(dropna=False, normalize=normalize)

        all_cats = sorted(set(real_counts.index).union(set(synth_counts.index)), key=lambda x: str(x))

        rows = []
        for cat in all_cats:
            real_val = float(real_counts.get(cat, 0.0))
            synth_val = float(synth_counts.get(cat, 0.0))
            rows.append(
                {
                    "category": cat,
                    "real": real_val,
                    "synthetic": synth_val,
                    "abs_diff": abs(real_val - synth_val),
                }
            )

        df_cat = pd.DataFrame(rows).set_index("category")
        df_cat = df_cat.sort_values("abs_diff", ascending=False).head(max_categories)
        results[col] = df_cat

    return results


# ----------------------------------------------------------------------
# 4) Marginals: lightweight histogram-style comparison
# ----------------------------------------------------------------------


def compare_marginals(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    n_bins: int = 20,
    max_categories: int = 20,
) -> Dict[str, Any]:
    """
    Compare one-dimensional marginals for each column.

    For numeric columns:
        - Use a common set of bins based on the combined data.
        - Return normalized histogram (probabilities) for real and synthetic.

    For categorical columns:
        - Return normalized value counts.

    Returns a dict: {column_name: {...}} where each value is:
        For numeric:
            {
                "type": "numeric",
                "bins": np.ndarray,  # bin edges
                "real_prob": np.ndarray,
                "synthetic_prob": np.ndarray,
            }
        For categorical:
            {
                "type": "categorical",
                "table": pd.DataFrame  # same format as compare_category_frequencies
            }
    """
    cols = _get_common_columns(real_df, synth_df, columns)
    out: Dict[str, Any] = {}

    for col in cols:
        real_col = real_df[col].dropna()
        synth_col = synth_df[col].dropna()
        col_type = _infer_col_type(real_col, max_categories=max_categories)

        if col_type == "numeric":
            combined = pd.concat([real_col, synth_col], axis=0)
            if combined.empty:
                continue

            bins = np.histogram_bin_edges(combined.to_numpy(), bins=n_bins)

            real_counts, _ = np.histogram(real_col.to_numpy(), bins=bins)
            synth_counts, _ = np.histogram(synth_col.to_numpy(), bins=bins)

            real_prob = real_counts / real_counts.sum() if real_counts.sum() > 0 else real_counts
            synth_prob = synth_counts / synth_counts.sum() if synth_counts.sum() > 0 else synth_counts

            out[col] = {
                "type": "numeric",
                "bins": bins,
                "real_prob": real_prob,
                "synthetic_prob": synth_prob,
            }

        elif col_type == "categorical":
            freq_table = compare_category_frequencies(
                real_df[[col]],
                synth_df[[col]],
                columns=[col],
                normalize=True,
                max_categories=max_categories,
            )[col]

            out[col] = {
                "type": "categorical",
                "table": freq_table,
            }

        # silently skip "other" columns (e.g. free text)

    return out

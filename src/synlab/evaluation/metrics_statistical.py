# ----------------------------------------------------------------------
# Statistical distribution metrics for synthetic data evaluation
# ----------------------------------------------------------------------


from __future__ import annotations

from typing import Dict, List, Optional, Any

import numpy as np
import pandas as pd

from pandas.api.types import is_numeric_dtype

# Reuse helpers from basic metrics
from .metrics_basic import _get_common_columns, _infer_col_type

# Optional: SciPy for KS test + Wasserstein
try:
    from scipy.stats import ks_2samp, wasserstein_distance as _wasserstein_distance

    _HAVE_SCIPY = True
except ImportError:  # pragma: no cover - pure fallback
    _HAVE_SCIPY = False


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------


def _js_divergence(p: np.ndarray, q: np.ndarray, base: float = 2.0) -> float:
    """
    Jensen–Shannon divergence between two discrete distributions.

    p, q: 1D arrays that sum to 1 (or close).
    Returns a finite, symmetric divergence in [0, log(base)].
    """
    p = p.astype(float)
    q = q.astype(float)

    # Normalize just in case
    p_sum = p.sum()
    q_sum = q.sum()
    if p_sum > 0:
        p = p / p_sum
    if q_sum > 0:
        q = q / q_sum

    m = 0.5 * (p + q)

    def _kl_div(a, b):
        # Safe KL with masking of zero entries
        mask = (a > 0) & (b > 0)
        a_safe = a[mask]
        b_safe = b[mask]
        return np.sum(a_safe * (np.log(a_safe) - np.log(b_safe))) / np.log(base)

    js = 0.5 * _kl_div(p, m) + 0.5 * _kl_div(q, m)
    return float(js)


def _kl_divergence(p: np.ndarray, q: np.ndarray, base: float = 2.0) -> float:
    """
    KL divergence D_KL(p || q) between discrete distributions p and q.
    Both p and q must be non-negative and sum to 1.

    Uses smoothing to avoid infinities:
        p' = (p + eps) / (1 + eps*k)
        q' = (q + eps) / (1 + eps*k)
    where k = len(p)

    Returns a finite KL value using log base `base`.
    """
    eps = 1e-12
    p = p.astype(float)
    q = q.astype(float)

    k = len(p)

    p_sm = (p + eps) / (1.0 + eps * k)
    q_sm = (q + eps) / (1.0 + eps * k)

    return float(np.sum(p_sm * (np.log(p_sm) - np.log(q_sm))) / np.log(base))


def _wasserstein_fallback(x: np.ndarray, y: np.ndarray) -> float:
    """
    Simple 1D Wasserstein distance implementation for the case when SciPy is unavailable.
    Based on sorting and integrating the absolute difference between empirical CDFs.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    x = x[~np.isnan(x)]
    y = y[~np.isnan(y)]
    if x.size == 0 or y.size == 0:
        return np.nan

    x_sorted = np.sort(x)
    y_sorted = np.sort(y)

    # Build a common grid of quantiles
    n = max(len(x_sorted), len(y_sorted))
    q = (np.arange(1, n + 1) - 0.5) / n

    # Interpolate inverse CDF (quantile function) on that grid
    x_q = np.quantile(x_sorted, q)
    y_q = np.quantile(y_sorted, q)

    # 1D Wasserstein is the mean absolute difference between quantiles
    return float(np.mean(np.abs(x_q - y_q)))


def _wasserstein_distance(x: np.ndarray, y: np.ndarray) -> float:
    """
    Wrapper that uses SciPy if available, otherwise a simple fallback.
    """
    if _HAVE_SCIPY:
        return float(_wasserstein_distance(x, y))
    return _wasserstein_fallback(x, y)


# ----------------------------------------------------------------------
# 1) Numeric: KS + Wasserstein per column
# ----------------------------------------------------------------------


def numeric_distribution_distances(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    min_unique: int = 5,
) -> pd.DataFrame:
    """
    Compute distribution distances for numeric columns:
        - Kolmogorov–Smirnov statistic (+ p-value if SciPy is available)
        - 1D Wasserstein distance

    Returns a DataFrame indexed by column with columns:
        ks_stat, ks_pvalue, wasserstein
    """
    cols = _get_common_columns(real_df, synth_df, columns)
    rows = []

    for col in cols:
        r = real_df[col]
        s = synth_df[col]

        if not (is_numeric_dtype(r) and is_numeric_dtype(s)):
            continue

        # If basically constant, KS/Wasserstein aren’t informative
        if r.nunique(dropna=True) < min_unique and s.nunique(dropna=True) < min_unique:
            rows.append(
                {
                    "column": col,
                    "ks_stat": np.nan,
                    "ks_pvalue": np.nan,
                    "wasserstein": 0.0,
                }
            )
            continue

        r_clean = r.dropna().to_numpy()
        s_clean = s.dropna().to_numpy()

        if r_clean.size == 0 or s_clean.size == 0:
            rows.append(
                {
                    "column": col,
                    "ks_stat": np.nan,
                    "ks_pvalue": np.nan,
                    "wasserstein": np.nan,
                }
            )
            continue

        if _HAVE_SCIPY:
            ks_res = ks_2samp(r_clean, s_clean, alternative="two-sided", mode="auto")
            ks_stat = float(ks_res.statistic)
            ks_pvalue = float(ks_res.pvalue)
        else:
            # crude KS statistic without p-value
            all_vals = np.sort(np.unique(np.concatenate([r_clean, s_clean])))
            r_cdf = np.searchsorted(np.sort(r_clean), all_vals, side="right") / r_clean.size
            s_cdf = np.searchsorted(np.sort(s_clean), all_vals, side="right") / s_clean.size
            ks_stat = float(np.max(np.abs(r_cdf - s_cdf)))
            ks_pvalue = np.nan

        wdist = _wasserstein_distance(r_clean, s_clean)

        rows.append(
            {
                "column": col,
                "ks_stat": ks_stat,
                "ks_pvalue": ks_pvalue,
                "wasserstein": wdist,
            }
        )

    if not rows:
        return pd.DataFrame(columns=["ks_stat", "ks_pvalue", "wasserstein"])

    df_out = pd.DataFrame(rows).set_index("column")
    return df_out.sort_values("wasserstein", ascending=False)


# ----------------------------------------------------------------------
# 2) Categorical: JS divergence per column
# ----------------------------------------------------------------------


def categorical_js_divergence(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    max_categories: int = 50,
    base: float = 2.0,
) -> pd.DataFrame:
    """
    Compute Jensen–Shannon divergence between categorical distributions
    for each categorical column.

    Returns a DataFrame indexed by column with:
        js_divergence, n_categories
    """
    cols = _get_common_columns(real_df, synth_df, columns)
    rows = []

    for col in cols:
        r = real_df[col]
        s = synth_df[col]

        col_type = _infer_col_type(r, max_categories=max_categories)
        if col_type != "categorical":
            continue

        r_counts = r.value_counts(dropna=False, normalize=True)
        s_counts = s.value_counts(dropna=False, normalize=True)

        all_cats = sorted(set(r_counts.index).union(set(s_counts.index)), key=lambda x: str(x))
        if len(all_cats) == 0:
            continue

        p = np.array([r_counts.get(cat, 0.0) for cat in all_cats], dtype=float)
        q = np.array([s_counts.get(cat, 0.0) for cat in all_cats], dtype=float)

        js = _js_divergence(p, q, base=base)

        rows.append(
            {
                "column": col,
                "js_divergence": js,
                "n_categories": len(all_cats),
            }
        )

    if not rows:
        return pd.DataFrame(columns=["js_divergence", "n_categories"])

    df_out = pd.DataFrame(rows).set_index("column")
    return df_out.sort_values("js_divergence", ascending=False)


def categorical_kl_divergence(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    max_categories: int = 50,
    base: float = 2.0,
) -> pd.DataFrame:
    """
    Compute KL divergence D_KL(real || synth) for each categorical column.

    Returns DataFrame with:
        kl_real_to_synth, kl_synth_to_real, js_divergence, n_categories
    """
    cols = _get_common_columns(real_df, synth_df, columns)
    rows = []

    for col in cols:
        r = real_df[col]
        s = synth_df[col]

        col_type = _infer_col_type(r, max_categories=max_categories)
        if col_type != "categorical":
            continue

        r_counts = r.value_counts(dropna=False, normalize=True)
        s_counts = s.value_counts(dropna=False, normalize=True)

        all_cats = sorted(set(r_counts.index).union(set(s_counts.index)), key=lambda x: str(x))

        p = np.array([r_counts.get(cat, 0.0) for cat in all_cats], dtype=float)
        q = np.array([s_counts.get(cat, 0.0) for cat in all_cats], dtype=float)

        kl_rs = _kl_divergence(p, q, base=base)
        kl_sr = _kl_divergence(q, p, base=base)
        js = _js_divergence(p, q, base=base)

        rows.append(
            {
                "column": col,
                "kl_real_to_synth": kl_rs,
                "kl_synth_to_real": kl_sr,
                "js_divergence": js,
                "n_categories": len(all_cats),
            }
        )

    if not rows:
        return pd.DataFrame(
            columns=[
                "kl_real_to_synth",
                "kl_synth_to_real",
                "js_divergence",
                "n_categories",
            ]
        )

    df_out = pd.DataFrame(rows).set_index("column")
    return df_out.sort_values("kl_real_to_synth", ascending=False)


# ----------------------------------------------------------------------
# 3) Correlation structure distance
# ----------------------------------------------------------------------


def correlation_structure_distance(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    method: str = "pearson",
) -> Dict[str, Any]:
    """
    Compare correlation structure between real and synthetic data.

    - Selects numeric columns.
    - Computes correlation matrices for real and synthetic.
    - Returns:
        {
            "real_corr": DataFrame,
            "synthetic_corr": DataFrame,
            "abs_diff": DataFrame,
            "frobenius_norm": float,
            "mean_abs_diff": float,
        }
    """
    if columns is None:
        # Intersect numeric columns
        real_num = [c for c in real_df.columns if is_numeric_dtype(real_df[c])]
        synth_num = [c for c in synth_df.columns if is_numeric_dtype(synth_df[c])]
        cols = [c for c in real_num if c in synth_num]
    else:
        cols = columns

    if not cols:
        return {
            "real_corr": pd.DataFrame(),
            "synthetic_corr": pd.DataFrame(),
            "abs_diff": pd.DataFrame(),
            "frobenius_norm": np.nan,
            "mean_abs_diff": np.nan,
        }

    r_corr = real_df[cols].corr(method=method)
    s_corr = synth_df[cols].corr(method=method)

    # Align just in case
    r_corr = r_corr.loc[cols, cols]
    s_corr = s_corr.loc[cols, cols]

    diff = r_corr - s_corr
    abs_diff = diff.abs()

    # Frobenius norm = sqrt(sum_ij diff_ij^2)
    frob = float(np.sqrt(np.square(diff.values).sum()))
    mean_abs = float(abs_diff.values.mean())

    return {
        "real_corr": r_corr,
        "synthetic_corr": s_corr,
        "abs_diff": abs_diff,
        "frobenius_norm": frob,
        "mean_abs_diff": mean_abs,
    }


# ----------------------------------------------------------------------
# 4) Unified univariate summary (numeric + categorical)
# ----------------------------------------------------------------------


def univariate_distribution_summary(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    max_categories: int = 50,
) -> pd.DataFrame:
    """
    Produce a unified summary of univariate distribution similarity
    for each column:

      - For numeric: ks_stat, ks_pvalue, wasserstein
      - For categorical: js_divergence, kl_real_to_synth, kl_synth_to_real

    Returns a DataFrame indexed by column with a 'type' column and
    the relevant metrics.
    """
    cols = _get_common_columns(real_df, synth_df, columns)

    # Numeric metrics
    num_dists = numeric_distribution_distances(real_df, synth_df, columns=cols)

    # Categorical metrics (includes JS + KL)
    cat_dists = categorical_kl_divergence(
        real_df,
        synth_df,
        columns=cols,
        max_categories=max_categories,
    )

    rows = []

    # Numeric rows
    for col, row in num_dists.iterrows():
        rows.append(
            {
                "column": col,
                "type": "numeric",
                "ks_stat": row["ks_stat"],
                "ks_pvalue": row["ks_pvalue"],
                "wasserstein": row["wasserstein"],
                "js_divergence": np.nan,
                "kl_real_to_synth": np.nan,
                "kl_synth_to_real": np.nan,
            }
        )

    # Categorical rows
    for col, row in cat_dists.iterrows():
        rows.append(
            {
                "column": col,
                "type": "categorical",
                "ks_stat": np.nan,
                "ks_pvalue": np.nan,
                "wasserstein": np.nan,
                "js_divergence": row["js_divergence"],
                "kl_real_to_synth": row["kl_real_to_synth"],
                "kl_synth_to_real": row["kl_synth_to_real"],
            }
        )

    if not rows:
        return pd.DataFrame(
            columns=[
                "type",
                "ks_stat",
                "ks_pvalue",
                "wasserstein",
                "js_divergence",
                "kl_real_to_synth",
                "kl_synth_to_real",
            ]
        )

    out = pd.DataFrame(rows).set_index("column")
    return out.sort_values(["type"], ascending=True)

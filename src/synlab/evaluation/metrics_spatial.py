"""
Spatial evaluation metrics for synthetic geographic data.

Evaluates how well synthetic data preserves spatial patterns, clustering,
and geographic distributions.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist
from scipy.stats import wasserstein_distance


def spatial_distribution_comparison(
    real_df: pd.DataFrame, synth_df: pd.DataFrame, x_col: str = "X_2025", y_col: str = "Y_2025", n_bins: int = 50
) -> Dict[str, float]:
    """
    Compare spatial distributions using 2D histogram comparison.

    Parameters
    ----------
    real_df : pd.DataFrame
        Real data with spatial coordinates.
    synth_df : pd.DataFrame
        Synthetic data with spatial coordinates.
    x_col, y_col : str
        Column names for X and Y coordinates.
    n_bins : int
        Number of bins for 2D histogram.

    Returns
    -------
    dict
        Dictionary with:
        - 'spatial_js_divergence': Jensen-Shannon divergence of 2D distributions
        - 'x_wasserstein': Wasserstein distance for X coordinates
        - 'y_wasserstein': Wasserstein distance for Y coordinates
    """
    # Get coordinates
    real_x = real_df[x_col].dropna().values
    real_y = real_df[y_col].dropna().values
    synth_x = synth_df[x_col].dropna().values
    synth_y = synth_df[y_col].dropna().values

    # Define common bins based on real data range
    x_bins = np.linspace(real_x.min(), real_x.max(), n_bins + 1)
    y_bins = np.linspace(real_y.min(), real_y.max(), n_bins + 1)

    # Compute 2D histograms
    real_hist, _, _ = np.histogram2d(real_x, real_y, bins=[x_bins, y_bins])
    synth_hist, _, _ = np.histogram2d(synth_x, synth_y, bins=[x_bins, y_bins])

    # Normalize to probability distributions
    real_hist = real_hist.flatten() / real_hist.sum()
    synth_hist = synth_hist.flatten() / synth_hist.sum()

    # Compute JS divergence
    js_div = _js_divergence(real_hist, synth_hist)

    # Compute Wasserstein distances for each dimension
    x_wasser = wasserstein_distance(real_x, synth_x)
    y_wasser = wasserstein_distance(real_y, synth_y)

    return {"spatial_js_divergence": float(js_div), "x_wasserstein": float(x_wasser), "y_wasserstein": float(y_wasser)}


def nearest_neighbor_distance_ratio(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    x_col: str = "X_2025",
    y_col: str = "Y_2025",
    n_sample: int = 1000,
    random_state: int = 42,
) -> Dict[str, float]:
    """
    Compare nearest neighbor distance distributions.

    Measures how well synthetic data preserves local density patterns
    by comparing nearest neighbor distances.

    Parameters
    ----------
    real_df, synth_df : pd.DataFrame
        Real and synthetic data with coordinates.
    x_col, y_col : str
        Column names for coordinates.
    n_sample : int
        Number of points to sample for efficiency.
    random_state : int
        Random seed for sampling.

    Returns
    -------
    dict
        Dictionary with:
        - 'nn_distance_ratio': Ratio of mean NN distances (synth/real)
        - 'nn_distance_wasserstein': Wasserstein distance between NN distributions
    """
    np.random.seed(random_state)

    # Sample points for efficiency
    real_sample = real_df[[x_col, y_col]].dropna().sample(n=min(n_sample, len(real_df)), random_state=random_state)
    synth_sample = synth_df[[x_col, y_col]].dropna().sample(n=min(n_sample, len(synth_df)), random_state=random_state)

    # Compute pairwise distances
    real_coords = real_sample.values
    synth_coords = synth_sample.values

    real_dists = cdist(real_coords, real_coords)
    synth_dists = cdist(synth_coords, synth_coords)

    # Get nearest neighbor distances (excluding self = 0)
    np.fill_diagonal(real_dists, np.inf)
    np.fill_diagonal(synth_dists, np.inf)

    real_nn = real_dists.min(axis=1)
    synth_nn = synth_dists.min(axis=1)

    # Compute metrics
    nn_ratio = float(synth_nn.mean() / real_nn.mean())
    nn_wasser = wasserstein_distance(real_nn, synth_nn)

    return {"nn_distance_ratio": nn_ratio, "nn_distance_wasserstein": float(nn_wasser)}


def spatial_autocorrelation_comparison(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    value_col: str,
    x_col: str = "X_2025",
    y_col: str = "Y_2025",
    n_bins: int = 20,
) -> Dict[str, float]:
    """
    Compare spatial autocorrelation patterns using binned correlations.

    Measures how attribute values correlate with spatial proximity.

    Parameters
    ----------
    real_df, synth_df : pd.DataFrame
        Real and synthetic data.
    value_col : str
        Column name of the attribute to analyze (e.g., industry code as numeric).
    x_col, y_col : str
        Coordinate column names.
    n_bins : int
        Number of distance bins for correlation analysis.

    Returns
    -------
    dict
        Dictionary with:
        - 'autocorr_difference': Mean absolute difference in autocorrelation by distance
    """

    def compute_binned_autocorr(df, value_col, x_col, y_col, n_bins):
        # Sample for efficiency
        sample_size = min(500, len(df))
        df_sample = df[[value_col, x_col, y_col]].dropna().sample(n=sample_size, random_state=42)

        coords = df_sample[[x_col, y_col]].values
        values = df_sample[value_col].values

        # Compute all pairwise distances
        dists = cdist(coords, coords)
        np.fill_diagonal(dists, np.nan)

        # Create distance bins
        max_dist = np.nanmax(dists)
        bins = np.linspace(0, max_dist, n_bins + 1)

        # Compute correlation for each distance bin
        autocorrs = []
        for i in range(n_bins):
            mask = (dists >= bins[i]) & (dists < bins[i + 1])
            if mask.sum() > 10:  # Need enough pairs
                idx = np.where(mask)
                corr = np.corrcoef(values[idx[0]], values[idx[1]])[0, 1]
                if not np.isnan(corr):
                    autocorrs.append(corr)
                else:
                    autocorrs.append(0.0)
            else:
                autocorrs.append(0.0)

        return np.array(autocorrs)

    # Compute for both datasets
    real_autocorr = compute_binned_autocorr(real_df, value_col, x_col, y_col, n_bins)
    synth_autocorr = compute_binned_autocorr(synth_df, value_col, x_col, y_col, n_bins)

    # Compare
    autocorr_diff = float(np.mean(np.abs(real_autocorr - synth_autocorr)))

    return {"spatial_autocorr_difference": autocorr_diff}


def geographic_unit_preservation(
    real_df: pd.DataFrame, synth_df: pd.DataFrame, unit_col: str = "grk2025"
) -> Dict[str, float]:
    """
    Evaluate preservation of geographic unit (BSU/grid cell) distributions.

    Parameters
    ----------
    real_df, synth_df : pd.DataFrame
        Real and synthetic data.
    unit_col : str
        Column name for geographic units (e.g., 'grk2025' for BSU).

    Returns
    -------
    dict
        Dictionary with:
        - 'unit_js_divergence': JS divergence of unit distributions
        - 'unit_overlap': Proportion of real units present in synthetic data
        - 'unit_count_correlation': Correlation of counts per unit
    """
    # Get unit distributions
    real_counts = real_df[unit_col].value_counts()
    synth_counts = synth_df[unit_col].value_counts()

    # Align on common units
    all_units = sorted(set(real_counts.index) | set(synth_counts.index))
    real_dist = np.array([real_counts.get(u, 0) for u in all_units], dtype=float)
    synth_dist = np.array([synth_counts.get(u, 0) for u in all_units], dtype=float)

    # Normalize
    real_dist = real_dist / real_dist.sum()
    synth_dist = synth_dist / synth_dist.sum()

    # JS divergence
    js_div = _js_divergence(real_dist, synth_dist)

    # Unit overlap
    real_units = set(real_counts.index)
    synth_units = set(synth_counts.index)
    overlap = len(real_units & synth_units) / len(real_units) if len(real_units) > 0 else 0.0

    # Correlation of counts (for overlapping units)
    common_units = sorted(real_units & synth_units)
    if len(common_units) > 1:
        real_common = [real_counts[u] for u in common_units]
        synth_common = [synth_counts[u] for u in common_units]
        count_corr = float(np.corrcoef(real_common, synth_common)[0, 1])
    else:
        count_corr = 0.0

    return {"unit_js_divergence": float(js_div), "unit_overlap": float(overlap), "unit_count_correlation": count_corr}


def _js_divergence(p: np.ndarray, q: np.ndarray, base: float = 2.0) -> float:
    """Jensen-Shannon divergence between two discrete distributions."""
    p = p.astype(float)
    q = q.astype(float)

    # Normalize
    p_sum = p.sum()
    q_sum = q.sum()
    if p_sum > 0:
        p = p / p_sum
    if q_sum > 0:
        q = q / q_sum

    m = 0.5 * (p + q)

    def _kl_div(a, b):
        mask = (a > 0) & (b > 0)
        a_safe = a[mask]
        b_safe = b[mask]
        if len(a_safe) == 0:
            return 0.0
        return np.sum(a_safe * (np.log(a_safe) - np.log(b_safe))) / np.log(base)

    js = 0.5 * _kl_div(p, m) + 0.5 * _kl_div(q, m)
    return float(js)


def evaluate_spatial_metrics(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    x_col: str = "X_2025",
    y_col: str = "Y_2025",
    unit_col: str = "grk2025",
    categorical_col: str = "orgf2025",
) -> pd.DataFrame:
    """
    Comprehensive spatial evaluation combining multiple metrics.

    Parameters
    ----------
    real_df, synth_df : pd.DataFrame
        Real and synthetic business data.
    x_col, y_col : str
        Coordinate columns.
    unit_col : str
        Geographic unit column (BSU/grid cell).
    categorical_col : str
        Categorical attribute for autocorrelation analysis.

    Returns
    -------
    pd.DataFrame
        DataFrame with all spatial metrics.
    """
    results = {}

    # 1. Spatial distribution
    results.update(spatial_distribution_comparison(real_df, synth_df, x_col, y_col))

    # 2. Nearest neighbor
    results.update(nearest_neighbor_distance_ratio(real_df, synth_df, x_col, y_col))

    # 3. Geographic units
    results.update(geographic_unit_preservation(real_df, synth_df, unit_col))

    # 4. Spatial autocorrelation (if categorical col can be converted to numeric)
    if categorical_col in real_df.columns and categorical_col in synth_df.columns:
        try:
            # Convert categorical to numeric codes for correlation
            real_df_copy = real_df.copy()
            synth_df_copy = synth_df.copy()
            real_df_copy[f"{categorical_col}_code"] = pd.Categorical(real_df_copy[categorical_col]).codes
            synth_df_copy[f"{categorical_col}_code"] = pd.Categorical(synth_df_copy[categorical_col]).codes

            results.update(
                spatial_autocorrelation_comparison(real_df_copy, synth_df_copy, f"{categorical_col}_code", x_col, y_col)
            )
        except Exception:
            # Skip if conversion fails
            pass

    return pd.DataFrame([results])

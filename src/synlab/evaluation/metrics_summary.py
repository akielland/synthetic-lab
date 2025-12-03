# 
def evaluate_all_metrics(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    target_col: Optional[str] = None,
    columns: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Convenience wrapper to compute a broad set of metrics
    in one call. Returns a nested dict of results.
    """
    basic_missing = compare_missingness(real_df, synth_df, columns=columns)
    basic_stats = compare_basic_stats(real_df, synth_df, columns=columns)
    cat_freqs = compare_category_frequencies(real_df, synth_df, columns=columns)
    marginals = compare_marginals(real_df, synth_df, columns=columns)

    uni = univariate_distribution_summary(real_df, synth_df, columns=columns)
    corr = correlation_structure_distance(real_df, synth_df, columns=columns)

    try:
        disc = discriminative_score(real_df, synth_df, columns=columns)
    except RuntimeError:
        disc = None

    tstr = None
    baseline = None
    if target_col is not None:
        try:
            tstr = tstr_classification(real_df, synth_df, target_col=target_col, feature_columns=columns)
            baseline = real_baseline_classification(real_df, target_col=target_col, feature_columns=columns)
        except RuntimeError:
            tstr = None
            baseline = None

    return {
        "basic": {
            "missingness": basic_missing,
            "basic_stats": basic_stats,
            "category_frequencies": cat_freqs,
            "marginals": marginals,
        },
        "statistical": {
            "univariate": uni,
            "correlation": corr,
        },
        "ml": {
            "discriminative": disc,
            "tstr_classification": tstr,
            "real_baseline_classification": baseline,
        },
    }

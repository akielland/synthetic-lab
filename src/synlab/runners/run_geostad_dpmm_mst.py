"""
Runner script for generating synthetic GeoSTAD business data using DPMM-MST.

This script:
1. Loads the GeoSTAD business registry data
2. Applies DPMM-MST synthesizer with differential privacy
3. Generates synthetic business locations
4. Evaluates synthetic data quality using spatial metrics
5. Saves results to outputs/synthetic/population/
"""

from synlab.data import load_geostad, prepare_for_synthesis
from synlab.data.configs import GeoSTADConfig
from synlab.evaluation import (
    compare_basic_stats,
    compare_category_frequencies,
    evaluate_spatial_metrics,
)
from synlab.methods import DPMMMSTConfig, DPMMMSTSynthesizer
from synlab.utils.paths import get_project_root


def main() -> None:
    """Run GeoSTAD synthetic data generation pipeline."""

    # ========================================
    # 1. Configuration
    # ========================================

    # Experiment settings
    experiment_name = "geostad_dpmm_mst_e1"
    n_synthetic = 5000
    random_state = 42

    # Method configuration (DPMM-MST specific privacy parameters)
    method_config = DPMMMSTConfig(
        epsilon=1.0,  # Privacy budget
        delta=1e-5,  # Privacy failure probability
        proc_epsilon=0.1,  # Processing epsilon for DPMM
    )

    # Data configuration
    data_config = GeoSTADConfig()

    print("=" * 60)
    print("GeoSTAD Synthetic Data Generation")
    print("=" * 60)
    print(f"Experiment: {experiment_name}")
    print(f"Target synthetic records: {n_synthetic:,}")
    print(f"Privacy: ε={method_config.epsilon}, δ={method_config.delta}")
    print()

    # ========================================
    # 2. Load and prepare data
    # ========================================
    print("Loading GeoSTAD data...")
    df_real, domain = load_geostad(config=data_config)

    print(f"Real data: {len(df_real):,} businesses")
    print(f"Columns: {df_real.columns.tolist()}")
    print()

    # Prepare for synthesis (select feature columns from config)
    df_features = prepare_for_synthesis(df_real, config=data_config, sample_size=None)
    print(f"Feature columns: {df_features.columns.tolist()}")
    print()

    # ========================================
    # 3. Create synthesizer
    # ========================================
    print("Configuring DPMM-MST synthesizer...")
    synthesizer = DPMMMSTSynthesizer(method_config)

    # ========================================
    # 4. Fit synthesizer
    # ========================================
    print("Fitting synthesizer on real data...")
    synthesizer.fit(df_features, domain)
    print("✓ Fit complete")
    print()

    # ========================================
    # 5. Generate synthetic data
    # ========================================
    print(f"Generating {n_synthetic:,} synthetic records...")
    df_synth = synthesizer.generate(n_synthetic, random_state=random_state)
    print(f"✓ Generated synthetic data: {df_synth.shape}")
    print()

    # ========================================
    # 6. Evaluate quality
    # ========================================
    print("Evaluating synthetic data quality...")
    print("-" * 60)

    # Basic statistics
    print("\n[Basic Statistics]")
    basic_stats = compare_basic_stats(df_features, df_synth)
    print(basic_stats.to_string())

    # Categorical distributions
    print("\n[Categorical Distributions]")
    cat_cols = ["SN2025", "orgf2025", "fpnr2025", "grk2025"]
    for col in cat_cols:
        if col in df_synth.columns:
            cat_freq = compare_category_frequencies(df_features, df_synth, column=col, top_k=10)
            print(f"\n{col} (top 10):")
            print(cat_freq.to_string())

    # Spatial metrics
    if "X_2025" in df_synth.columns and "Y_2025" in df_synth.columns:
        print("\n[Spatial Metrics]")
        spatial_metrics = evaluate_spatial_metrics(
            df_features, df_synth, x_col="X_2025", y_col="Y_2025", unit_col="grk2025", categorical_col="orgf2025"
        )
        print(spatial_metrics.T.to_string())

    print()
    print("=" * 60)

    # ========================================
    # 7. Save results
    # ========================================
    root = get_project_root()
    out_dir = root / "outputs" / "synthetic" / "population" / experiment_name
    out_dir.mkdir(parents=True, exist_ok=True)

    # Save synthetic data
    df_synth.to_csv(out_dir / "synthetic.csv", index=False)
    print(f"✓ Saved synthetic data: {out_dir / 'synthetic.csv'}")

    # Save configuration
    config_text = (
        f"Experiment: {experiment_name}\n"
        f"Real records: {len(df_real):,}\n"
        f"Synthetic records: {n_synthetic:,}\n"
        f"Epsilon: {method_config.epsilon}\n"
        f"Delta: {method_config.delta}\n"
        f"Proc epsilon: {method_config.proc_epsilon}\n"
        f"Random state: {random_state}\n"
        f"Feature columns: {df_features.columns.tolist()}\n"
    )
    (out_dir / "config.txt").write_text(config_text)
    print(f"✓ Saved configuration: {out_dir / 'config.txt'}")

    # Save evaluation metrics
    if "X_2025" in df_synth.columns:
        spatial_metrics.to_csv(out_dir / "spatial_metrics.csv", index=False)
        print(f"✓ Saved spatial metrics: {out_dir / 'spatial_metrics.csv'}")

    print()
    print(f"All outputs saved to: {out_dir}")
    print("=" * 60)


if __name__ == "__main__":
    main()

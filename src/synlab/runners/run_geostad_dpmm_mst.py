"""
Runner script for generating synthetic GeoSTAD business data using DPMM-MST.

This script:
1. Loads the GeoSTAD business registry data
2. Applies DPMM-MST synthesizer with differential privacy
3. Generates synthetic business locations
4. Evaluates synthetic data quality using spatial metrics
5. Saves results to outputs/synthetic/population/
"""

from pathlib import Path

from synlab.core import ExperimentConfig
from synlab.data import load_geostad, prepare_for_synthesis
from synlab.evaluation import (
    compare_basic_stats,
    compare_category_frequencies,
    evaluate_spatial_metrics,
)
from synlab.methods import DPMMMSTConfig, DPMMMSTSynthesizer


def get_project_root() -> Path:
    """Get project root directory."""
    return Path(__file__).resolve().parents[3]


def main() -> None:
    """Run GeoSTAD synthetic data generation pipeline."""

    # ========================================
    # 1. Configuration
    # ========================================
    cfg = ExperimentConfig(
        name="geostad_dpmm_mst_e1",
        n_synth=5000,  # Generate 5k synthetic businesses
        epsilon=1.0,
        delta=1e-5,
        proc_epsilon=0.1,
        random_state=42,
    )

    print("=" * 60)
    print("GeoSTAD Synthetic Data Generation")
    print("=" * 60)
    print(f"Experiment: {cfg.name}")
    print(f"Target synthetic records: {cfg.n_synth:,}")
    print(f"Privacy: ε={cfg.epsilon}, δ={cfg.delta}")
    print()

    # ========================================
    # 2. Load and prepare data
    # ========================================
    print("Loading GeoSTAD data...")
    df_real, domain = load_geostad(filter_geocoded=True, remove_duplicates=True)

    print(f"Real data: {len(df_real):,} businesses")
    print(f"Columns: {df_real.columns.tolist()}")
    print()

    # Prepare for synthesis (select feature columns)
    df_features = prepare_for_synthesis(df_real, sample_size=None)
    print(f"Feature columns: {df_features.columns.tolist()}")
    print()

    # ========================================
    # 3. Create synthesizer
    # ========================================
    print("Configuring DPMM-MST synthesizer...")
    method_cfg = DPMMMSTConfig(
        epsilon=cfg.epsilon,
        delta=cfg.delta,
        proc_epsilon=cfg.proc_epsilon,
    )
    synthesizer = DPMMMSTSynthesizer(method_cfg)

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
    print(f"Generating {cfg.n_synth:,} synthetic records...")
    df_synth = synthesizer.generate(cfg.n_synth, random_state=cfg.random_state)
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
    out_dir = root / "outputs" / "synthetic" / "population" / cfg.name
    out_dir.mkdir(parents=True, exist_ok=True)

    # Save synthetic data
    df_synth.to_csv(out_dir / "synthetic.csv", index=False)
    print(f"✓ Saved synthetic data: {out_dir / 'synthetic.csv'}")

    # Save configuration
    config_text = (
        f"Experiment: {cfg.name}\n"
        f"Real records: {len(df_real):,}\n"
        f"Synthetic records: {cfg.n_synth:,}\n"
        f"Epsilon: {cfg.epsilon}\n"
        f"Delta: {cfg.delta}\n"
        f"Proc epsilon: {cfg.proc_epsilon}\n"
        f"Random state: {cfg.random_state}\n"
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

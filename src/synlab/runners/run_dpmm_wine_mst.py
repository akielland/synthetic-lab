from pathlib import Path

from synlab.data import load_dpmm_wine
from synlab.methods import DPMMMSTConfig, DPMMMSTSynthesizer
from synlab.utils.paths import get_project_root


def main() -> None:
    # 1. Experiment settings
    experiment_name = "dpmm_wine_mst_e1"
    n_synthetic = 1000
    random_state = 42

    # 2. Method configuration (DPMM-MST privacy parameters)
    method_cfg = DPMMMSTConfig(
        epsilon=1.0,
        delta=1e-5,
        proc_epsilon=0.1,
    )

    # 3. Load real data + domain
    df_real, domain = load_dpmm_wine()

    # 4. Build synthesizer
    synthesizer = DPMMMSTSynthesizer(method_cfg)

    # 5. Fit on real data
    synthesizer.fit(df_real, domain)

    # 6. Generate synthetic data
    df_synth = synthesizer.generate(n_synthetic, random_state=random_state)

    # 6. Basic sanity checks printed to console
    print("Real shape:     ", df_real.shape)
    print("Synthetic shape:", df_synth.shape)
    print("Real columns:   ", df_real.columns.tolist())
    print("Synthetic cols: ", df_synth.columns.tolist())

    # 7. Save results
    root = get_project_root()
    out_dir = root / "outputs" / "population" / experiment_name
    out_dir.mkdir(parents=True, exist_ok=True)

    df_synth.to_csv(out_dir / "synthetic.csv", index=False)

    # Save a tiny config snapshot for traceability
    (out_dir / "config.txt").write_text(repr(cfg))

    print(f"\nSaved synthetic data to: {out_dir / 'synthetic.csv'}")


if __name__ == "__main__":
    main()

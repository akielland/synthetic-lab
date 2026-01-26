from pathlib import Path

from synlab.core import ExperimentConfig
from synlab.data import load_dpmm_wine
from synlab.methods import DPMMMSTSynthesizer, DPMMMSTConfig
from synlab.utils.paths import get_project_root


def main() -> None:
    # 1. Define experiment configuration
    cfg = ExperimentConfig(
        name="dpmm_wine_mst_e1",
        n_synth=1000,
        epsilon=1.0,
        delta=1e-5,
        proc_epsilon=0.1,
        random_state=42,
    )

    # 2. Load real data + domain
    df_real, domain = load_dpmm_wine()

    # 3. Build method-specific config and synthesizer
    method_cfg = DPMMMSTConfig(
        epsilon=cfg.epsilon,
        delta=cfg.delta,
        proc_epsilon=cfg.proc_epsilon,
    )
    synthesizer = DPMMMSTSynthesizer(method_cfg)

    # 4. Fit on real data
    synthesizer.fit(df_real, domain)

    # 5. Generate synthetic data
    df_synth = synthesizer.generate(cfg.n_synth, random_state=cfg.random_state)

    # 6. Basic sanity checks printed to console
    print("Real shape:     ", df_real.shape)
    print("Synthetic shape:", df_synth.shape)
    print("Real columns:   ", df_real.columns.tolist())
    print("Synthetic cols: ", df_synth.columns.tolist())

    # 7. Save results
    root = get_project_root()
    out_dir = root / "outputs" / "population" / cfg.name
    out_dir.mkdir(parents=True, exist_ok=True)

    df_synth.to_csv(out_dir / "synthetic.csv", index=False)

    # Save a tiny config snapshot for traceability
    (out_dir / "config.txt").write_text(repr(cfg))

    print(f"\nSaved synthetic data to: {out_dir / 'synthetic.csv'}")


if __name__ == "__main__":
    main()

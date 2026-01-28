import time
from dataclasses import dataclass
from typing import Any, Optional

import pandas as pd
from dpmm.pipelines import MSTPipeline  # dpmm's own class

from synlab.core import BaseSynthesizer


@dataclass
class DPMMMSTConfig:
    """
    Configuration specific to the dpmm MST pipeline.
    """

    epsilon: float = 1.0
    delta: float = 1e-5
    proc_epsilon: float = 0.1


class DPMMMSTSynthesizer(BaseSynthesizer):
    """
    Adapter that makes dpmm's MSTPipeline look like a generic synthesizer.
    """

    def __init__(self, config: DPMMMSTConfig) -> None:
        self.config = config
        self._model: Optional[MSTPipeline] = None

    def fit(self, df: pd.DataFrame, domain: Any) -> None:
        """
        Create and fit the underlying MSTPipeline model.
        """
        print(f"\n{'=' * 70}")
        print(f"🚀 Starting DPMM-MST Training")
        print(f"{'=' * 70}")
        print(f"Dataset: {len(df):,} records × {len(df.columns)} features")
        print(f"Privacy: ε={self.config.epsilon}, δ={self.config.delta}")
        print(f"Processing ε={self.config.proc_epsilon}")
        print(f"\nThis may take 10-30 minutes with large datasets...")
        print(f"{'=' * 70}\n")

        start_time = time.time()

        print("⏳ Step 1/3: Initializing DPMM-MST pipeline...")
        self._model = MSTPipeline(
            epsilon=self.config.epsilon,
            delta=self.config.delta,
            proc_epsilon=self.config.proc_epsilon,
        )
        print("   ✓ Pipeline initialized")

        print("\n⏳ Step 2/3: Processing data and building privacy mechanisms...")
        print("   (This step includes binning, encoding, and DP noise addition)")

        self._model.fit(df, domain)

        elapsed = time.time() - start_time
        print(f"\n✓ Step 3/3: Training complete!")
        print(f"\n{'=' * 70}")
        print(f"✅ DPMM-MST training finished in {elapsed:.1f} seconds ({elapsed / 60:.1f} minutes)")
        print(f"{'=' * 70}\n")

    def generate(self, n: int, *, random_state: Optional[int] = None) -> pd.DataFrame:
        """
        Generate n synthetic records using the fitted MSTPipeline.
        """
        if self._model is None:
            raise RuntimeError("DPMMMSTSynthesizer.fit() must be called before generate().")

        print(f"\n{'=' * 70}")
        print(f"🎲 Generating Synthetic Data")
        print(f"{'=' * 70}")
        print(f"Target: {n:,} synthetic records")
        print(f"Random state: {random_state}")
        print(f"\n⏳ Sampling from trained model...")

        start_time = time.time()

        synth_df = self._model.generate(
            n_records=n,
            random_state=random_state,
        )

        elapsed = time.time() - start_time
        print(f"\n✅ Generation complete in {elapsed:.1f} seconds")
        print(f"   Generated: {len(synth_df):,} records × {len(synth_df.columns)} features")
        print(f"{'=' * 70}\n")

        return synth_df

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
        self._model = MSTPipeline(
            epsilon=self.config.epsilon,
            delta=self.config.delta,
            proc_epsilon=self.config.proc_epsilon,
        )
        self._model.fit(df, domain)

    def generate(self, n: int, *, random_state: Optional[int] = None) -> pd.DataFrame:
        """
        Generate n synthetic records using the fitted MSTPipeline.
        """
        if self._model is None:
            raise RuntimeError("DPMMMSTSynthesizer.fit() must be called before generate().")

        synth_df = self._model.generate(
            n_records=n,
            random_state=random_state,
        )
        return synth_df

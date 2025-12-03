from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional

import pandas as pd


@dataclass
class ExperimentConfig:
    """
    Configuration for a single synthetic-data experiment.

    This is deliberately small and generic. For now we keep
    dpmm-specific params here, but we can later move those into
    method-specific config dataclasses.
    """
    name: str                # used for naming output folder
    n_synth: int = 1000
    epsilon: float = 1.0
    delta: float = 1e-5
    proc_epsilon: float = 0.1
    random_state: Optional[int] = None


class BaseSynthesizer(ABC):
    """
    Abstract interface for all synthetic data generators.

    Every method should at least support:

    - fit(real_df, domain)
    - generate(n, random_state=...)

    so the rest of the lab can treat them uniformly.
    """

    @abstractmethod
    def fit(self, df: pd.DataFrame, domain: Any) -> None:
        """
        Train the synthesizer on real data and domain metadata.
        """

    @abstractmethod
    def generate(self, n: int, *, random_state: Optional[int] = None) -> pd.DataFrame:
        """
        Generate n synthetic records as a pandas DataFrame.
        """

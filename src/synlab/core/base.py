from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional

import pandas as pd


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

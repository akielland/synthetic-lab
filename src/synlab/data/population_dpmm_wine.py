import json
from pathlib import Path
from typing import Any, Dict, Tuple

import pandas as pd

from synlab.utils.paths import get_project_root


def load_dpmm_wine() -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Load the wine example dataset and its domain definition as used in the dpmm README.

    Returns
    -------
    df : pd.DataFrame
        Real wine dataset.
    domain : dict
        Domain metadata expected by dpmm (from wine_bounds.json).
    """
    root = get_project_root()
    wine_dir = root / "data" / "raw" / "population" / "dpmm_wine"

    df = pd.read_pickle(wine_dir / "wine.pkl.gz")
    with (wine_dir / "wine_bounds.json").open("r", encoding="utf-8") as f:
        domain = json.load(f)

    return df, domain

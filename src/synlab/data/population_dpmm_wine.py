from pathlib import Path
import json
from typing import Tuple, Dict, Any

import pandas as pd


def get_project_root() -> Path:
    """
    Return the root of the project (directory that contains src/, data/, outputs/, etc.).
    """
    # this file: src/synlab/data/population_dpmm_wine.py
    # parents[0] -> data/
    # parents[1] -> synlab/
    # parents[2] -> src/
    # parents[3] -> project root
    return Path(__file__).resolve().parents[3]


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

# get_project_root()
# src/synlab/utils/paths.py
from pathlib import Path


def get_project_root() -> Path:
    """
    Locate the project root directory.

    This file lives inside:
        project_root/src/synlab/utils/paths.py

    Therefore:
        parents[0] = utils/
        parents[1] = synlab/
        parents[2] = src/
        parents[3] = project_root/
    """
    return Path(__file__).resolve().parents[3]

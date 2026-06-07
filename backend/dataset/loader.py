import pandas as pd
from pathlib import Path


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV dataset.

    Args:
        file_path (str): Path to CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    return pd.read_csv(file_path)


def load_json(file_path: str) -> pd.DataFrame:
    """
    Load a JSON dataset.

    Args:
        file_path (str): Path to JSON file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    return pd.read_json(file_path)
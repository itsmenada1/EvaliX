import json
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "id",
    "input",
    "expected_output",
    "context",
    "task_type",
    "metadata"
]


def validate_schema(df: pd.DataFrame) -> None:
    """
    Validate dataset schema.

    Args:
        df (pd.DataFrame): Dataset.

    Raises:
        ValueError: If required columns are missing.
    """

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic dataset cleaning.

    - Remove empty rows
    - Remove duplicates
    - Strip whitespace

    Args:
        df (pd.DataFrame): Dataset.

    Returns:
        pd.DataFrame: Cleaned dataset.
    """

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill null values
    df["context"] = df["context"].fillna("")
    df["metadata"] = df["metadata"].fillna("{}")

    # Strip spaces from string columns
    for column in df.select_dtypes(include=["object"]).columns:
        df[column] = df[column].astype(str).str.strip()

    return df


def standardize_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reorder columns according to platform schema.

    Args:
        df (pd.DataFrame): Dataset.

    Returns:
        pd.DataFrame: Standardized dataset.
    """

    return df[
        [
            "id",
            "input",
            "expected_output",
            "context",
            "task_type",
            "metadata"
        ]
    ]


def save_processed_dataset(
    df: pd.DataFrame,
    output_path: str = "data/processed/standardized_dataset.json"
) -> None:
    """
    Save processed dataset as JSON.

    Args:
        df (pd.DataFrame): Dataset.
        output_path (str): Output file path.
    """

    output_file = Path(output_path)

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    records = df.to_dict(orient="records")

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            records,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"Processed dataset saved successfully to: {output_path}"
    )
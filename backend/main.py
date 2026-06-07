
# EPIC 1: Data Validation and Cleaning
from dataset.loader import load_csv
from dataset.validator import (
    validate_schema,
    clean_dataset,
    standardize_dataset,
    save_processed_dataset
)


def main():

    dataset_path = "data/raw/evaluation_dataset.csv"

    dataset = load_csv(dataset_path)

    validate_schema(dataset)

    dataset = clean_dataset(dataset)

    dataset = standardize_dataset(dataset)

    save_processed_dataset(dataset)

    print("EPIC 1 completed successfully.")


if __name__ == "__main__":
    main()
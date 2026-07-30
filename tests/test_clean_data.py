import pandas as pd

from bank_customer.extract.extract import extract
from bank_customer.transform.clean_df import clean_heads
from bank_customer.utils.paths import get_path_raw


def test_get_path():
    path_file = get_path_raw("dataset.csv")
    assert path_file.exists()
    assert path_file.name == "dataset.csv"
    assert "data" in path_file.parts
    assert "raw" in path_file.parts


def test_extract_data():
    path_file = get_path_raw("dataset.csv")
    assert path_file.exists()
    df = extract(path_file)
    assert isinstance(df, pd.DataFrame)


def test_clean_columns():
    expected_columns = {
        "month",
        "duration",
        "campaign",
        "pdays",
        "previous",
        "poutcome",
        "subscription",
    }

    df = extract(get_path_raw("dataset.csv"))
    original_columns = df.columns.copy()

    cleaned_df = clean_heads(df)

    assert expected_columns.issubset(cleaned_df.columns)
    assert "v11" not in cleaned_df.columns
    assert "class" not in cleaned_df.columns
    assert isinstance(cleaned_df, pd.DataFrame)
    assert cleaned_df is not df
    assert df.columns.equals(original_columns)

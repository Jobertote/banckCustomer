import pandas as pd
from bank_customer.utils.paths import get_path_raw
from bank_customer.extract.extract import extract
from bank_customer.transform.clean_df import clean_heads

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
    path_file = get_path_raw("dataset.csv")
    assert path_file.exists()
    df = extract(path_file)
    df = clean_heads(df)
    assert isinstance(df, pd.DataFrame)
    assert all(" " not in column for column in df.columns)
import pandas as pd
from bank_customer.extract.extract import extract
from bank_customer.transform.clean_df import clean_heads
from bank_customer.transform.transform import filter_by_column_over_under, filter_by_column_equal, get_keep_columns
from bank_customer.utils.paths import get_path_raw

def test_keep_columns():
    df = clean_heads(extract(get_path_raw('dataset.csv')))
    df = get_keep_columns(df, ['age'])
    assert all("age" in column for column in df.columns)
    assert all("average_yearly_balance" not in column for column in df.columns)

def test_filter_column_over():
    df = clean_heads(extract(get_path_raw('dataset.csv')))
    df = filter_by_column_over_under(df, 'age', True, 50)
    assert all(value > 50 for value in df['age'])

def test_filter_column_under():
    df = clean_heads(extract(get_path_raw('dataset.csv')))
    df = filter_by_column_over_under(df, 'age', False, 50)
    assert all(value < 50 for value in df['age'])

def test_filter_column_equal():
    df = clean_heads(extract(get_path_raw('dataset.csv')))
    df = filter_by_column_equal(df, 'age', 40)
    assert all(value == 40 for value in df['age'])
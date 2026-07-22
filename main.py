from bank_customer.utils.paths import get_path_raw
from bank_customer.extract.extract import extract
from bank_customer.transform.clean_df import clean_heads, keep_columns
from bank_customer.load.load import generate_clean_csv


def run_pipeline():
    df = keep_columns(clean_heads(extract(get_path_raw("dataset.csv"))))
    generate_clean_csv(df.head(100))
    print(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_pipeline()
from src.utils.paths import get_path_raw
from src.extract.extract import extract
from src.transform.clean_df import clean_heads, keep_columns
from src.transform.transform import get_default_calculations


def run_pipeline():
    df = get_default_calculations(keep_columns(clean_heads(extract(get_path_raw("dataset.csv")))))
    print(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prueba()

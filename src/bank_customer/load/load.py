import pandas as pd
from bank_customer.utils.paths import get_path_processed

def generate_clean_csv(df: pd.DataFrame):
    df.to_csv(get_path_processed("clean_dataset.csv"), index=False)
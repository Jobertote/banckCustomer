from pathlib import Path

import pandas as pd

from bank_customer.utils.paths import get_path_processed


def generate_clean_csv(df: pd.DataFrame) -> Path:
    output_path = get_path_processed("clean_dataset.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path

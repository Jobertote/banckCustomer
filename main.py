from pathlib import Path

from bank_customer.extract.extract import extract
from bank_customer.load.load import generate_clean_csv
from bank_customer.transform.clean_df import clean_heads
from bank_customer.utils.paths import get_path_raw


def run_pipeline() -> Path:
    input_path = get_path_raw("dataset.csv")
    df = clean_heads(extract(input_path))
    output_path = generate_clean_csv(df)

    print(f"Pipeline completado: {len(df):,} registros procesados.")
    print(f"Dataset limpio, guardado en: {output_path}")

    return output_path


if __name__ == "__main__":
    run_pipeline()

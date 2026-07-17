import pandas as pd

def extract(file_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_name)

    return df
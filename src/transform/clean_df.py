import pandas as pd

def clean_heads(df : pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(' ','_')
        .str.replace(',', '_')
        .str.replace('-','_')
        .str.replace('/','_'))
    return df

def keep_columns(df : pd.DataFrame) -> pd.DataFrame:
    df = df.iloc[:, :10]
    return df
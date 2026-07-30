import pandas as pd

COLUMNS_RENAMES = {
    "v11": "month",
    "v12": "duration",
    "v13": "campaign",
    "v14": "pdays",
    "v15": "previous",
    "v16": "poutcome",
    "class": "subscription",
}


def clean_heads(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()
    cleaned_df.columns = (
        cleaned_df.columns.str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace(",", "_")
        .str.replace("-", "_")
        .str.replace("/", "_")
    )
    return cleaned_df.rename(columns=COLUMNS_RENAMES)

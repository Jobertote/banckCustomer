import pandas as pd

KEEP_COLUMNS = [
    'age', 
    'type_of_job', 
    'marital_status', 
    'education_level',
    'credit_in_default', 
    'average_yearly_balance', 
    'housing_loan',
    'personal_loan', 
    'contact_communication_type',
    'last_contact_day_of_the_month'
]

def get_default_calculations(df : pd.DataFrame) -> pd.DataFrame:
    return df.describe()

def get_keep_columns(df: pd.DataFrame, columnas : list) -> pd.DataFrame:
    return df[columnas]

def filter_by_column_over_under(df : pd.DataFrame, column_name : str, over : bool, value : int) -> pd.DataFrame:
    if (over):
        df = df[df[column_name] > value]
    else:
        df = df[df[column_name] < value]
    return df

def filter_by_column_equal(df : pd.DataFrame, column_name : str, value : int) -> pd.DataFrame:
    return df[df[column_name] == value]

def get_principal_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df[KEEP_COLUMNS]

def filter_by_between_int(df : pd.DataFrame, column_name : str, value_ini : int, value_end : int) -> pd.DataFrame:
    return df[df[column_name].between(value_ini, value_end)]
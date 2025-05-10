import pandas as pd

def clean_missing_data(df, method='drop'):
    if method == 'drop':
        return df.dropna()
    elif method == 'mean':
        return df.fillna(df.mean(numeric_only=True))
    elif method == 'median':
        return df.fillna(df.median(numeric_only=True))
    else:
        raise ValueError("Invalid method. Choose 'drop', 'mean', or 'median'")
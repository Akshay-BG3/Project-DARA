import pandas as pd
import os


def check_file_format(file):
    ext = os.path.splitext(file.name)[-1].lower()
    if ext == ".csv":
        return 'csv'
    elif ext in [".xlsx", ".xls"]:
        return 'excel'
    elif ext == ".json":
        return 'json'
    else:
        return None

# Function to read dataset (based on the file format)
def read_dataset(file):
    file_format = check_file_format(file)
    if file_format == 'csv':
        return pd.read_csv(file)
    elif file_format == 'excel':
        return pd.read_excel(file)
    elif file_format == 'json':
        return pd.read_json(file)
    else:
        raise ValueError("Unsupported file format. Use CSV, Excel, or JSON")
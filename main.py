# main.py — Refactored (No FastAPI)

import pandas as pd
import os
from summary_generator import generate_summary
from visualization import generate_histogram, generate_scatter_plot
from functions import fig_to_base64
from ml_module import preprocess_data, train_model, predict as model_predict
import pickle
import base64

# Function to check file format (CSV, Excel, JSON)
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

# Function that replaces /summary/
def summarize_data(df):
    return generate_summary(df)

# Function that replaces /histogram/
def get_histogram(df, column):
    return fig_to_base64(generate_histogram(df, column))

# Function that replaces /scatter/
def get_scatter(df, x_column, y_column):
    return fig_to_base64(generate_scatter_plot(df, x_column, y_column))

# Function that replaces /train_model/
def train_and_serialize(df, target_column):
    X, y, scaler, label_encoders = preprocess_data(df, target_column)
    model, accuracy, report = train_model(X, y)

    model_bytes = base64.b64encode(pickle.dumps(model)).decode()
    scaler_bytes = base64.b64encode(pickle.dumps(scaler)).decode()
    encoder_bytes = base64.b64encode(pickle.dumps(label_encoders)).decode()

    return {
        "accuracy": accuracy,
        "report": report,
        "model_bytes": model_bytes,
        "scaler_bytes": scaler_bytes,
        "encoder_bytes": encoder_bytes,
        "feature_columns": list(X.columns)
    }

# Function that replaces /predict/
def make_prediction(model_b64, scaler_b64, encoder_b64, input_data):
    model = pickle.loads(base64.b64decode(model_b64))
    scaler = pickle.loads(base64.b64decode(scaler_b64))
    label_encoders = pickle.loads(base64.b64decode(encoder_b64))

    prediction = model_predict(model, scaler, label_encoders, input_data)
    return prediction[0]

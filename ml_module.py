# ml_module.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# 1. Data Preprocessing
def preprocess_data(df, target_column):
    """Preprocesses the dataset: handles encoding and scaling."""
    df = df.copy()

    # Encode categorical columns
    label_encoders = {}
    for col in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Separate features and target
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, label_encoders


# 2. Train Machine Learning Model
def train_model(X, y):
    """Trains a simple Logistic Regression model."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    return model, accuracy, report


# 3. Make Predictions
def predict(model, scaler, label_encoders, input_data):
    """Predicts using the trained model."""
    input_df = pd.DataFrame([input_data])

    # Encode if necessary
    for col, le in label_encoders.items():
        if col in input_df.columns:
            input_df[col] = le.transform(input_df[col])

    # Scale input
    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)
    return prediction


import pandas as pd

def generate_summary(df):
    summary = {}

    # Shape
    summary["Shape"] = {
        "Rows": df.shape[0],
        "Columns": df.shape[1]
    }

    # Data Types
    summary["Data Types"] = df.dtypes.value_counts().to_dict()

    # Column-wise details
    column_details = []
    for col in df.columns:
        data = {
            "Column": col,
            "Data Type": str(df[col].dtype),
            "Missing Values": df[col].isnull().sum(),
            "% Missing": round(df[col].isnull().mean() * 100, 2),
            "Unique Values": df[col].nunique(),
            "Skewness": df[col].skew() if df[col].dtype in ['int64', 'float64'] else None,
            "Kurtosis": df[col].kurtosis() if df[col].dtype in ['int64', 'float64'] else None
        }

        if df[col].dtype == 'object':
            data["Most Frequent"] = df[col].mode().iloc[0] if not df[col].mode().empty else "N/A"
        elif df[col].dtype in ['int64', 'float64']:
            data["Mean"] = df[col].mean()
            data["Median"] = df[col].median()
            data["Std Dev"] = df[col].std()
            data["Min"] = df[col].min()
            data["Max"] = df[col].max()
            # IQR (Interquartile Range)
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            data["IQR"] = IQR

        column_details.append(data)

    summary["Column Summary"] = column_details

    # Warnings
    warnings = []

    # High missing values
    for col in df.columns:
        missing_pct = df[col].isnull().mean()
        if missing_pct > 0.5:
            warnings.append(f"⚠️ Column '{col}' has over 50% missing values.")

    # Constant columns
    for col in df.columns:
        if df[col].nunique() == 1:
            warnings.append(f"⚠️ Column '{col}' has only one unique value (constant).")

    # High cardinality
    for col in df.select_dtypes(include='object').columns:
        if df[col].nunique() > 100:
            warnings.append(f"⚠️ Column '{col}' has high cardinality ({df[col].nunique()} unique values).")

    # Categorical imbalance check
    for col in df.select_dtypes(include='object').columns:
        value_counts = df[col].value_counts()
        if len(value_counts) > 1 and value_counts.min() / value_counts.max() < 0.05:
            warnings.append(f"⚠️ Column '{col}' has highly imbalanced categories.")

    summary["Warnings"] = warnings

    return summary



def display_summary(summary):
    print("\n📊 Dataset Summary:\n")

    print(f"Rows: {summary['Shape']['Rows']}, Columns: {summary['Shape']['Columns']}")
    print("\n🧾 Column Details:\n")

    for col in summary['Column Summary']:
        print(f"🔹 {col['Column']} ({col['Data Type']}):")
        print(f"   Missing: {col['Missing Values']} ({col['% Missing']}%)")
        print(f"   Unique Values: {col['Unique Values']}")

        if 'Most Frequent' in col:
            print(f"   Most Frequent: {col['Most Frequent']}")
        if 'Mean' in col:
            print(f"   Mean: {col['Mean']:.2f}, Median: {col['Median']:.2f}, Std: {col['Std Dev']:.2f}")
            print(f"   Min: {col['Min']}, Max: {col['Max']}")
        print()

    if summary["Warnings"]:
        print("\n🚨 Warnings:\n")
        for warning in summary["Warnings"]:
            print(warning)
    else:
        print("\n✅ No critical issues found in the dataset.\n")

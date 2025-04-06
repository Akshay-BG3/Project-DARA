import pandas as pd
import os

def check_file_format(file_path):
    if file_path.endswith(".csv"):
        return 'csv'
    elif file_path.endswith(".xlsx"):
        return 'excel'
    elif file_path.endswith(".json"):
        return 'json'
    else:
        raise ValueError("Unsupported file format. Please upload .csv, .xlcs, .json file")

def read_dataset(file_path):

    file_format = check_file_format(file_path)

    if file_format == 'csv':
        return pd.read_csv(file_path)
    elif file_format == 'excel':
        return pd.read_excel(file_path)
    elif file_format == 'json':
        return pd.read_json(file_path)

def load_dataset(file_path):

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file at {file_path} does not exist.")

        df = read_dataset(file_path)
        print("Successfully loaded the dataset!")

        print("Basic information")
        print(df.info())

        print("First 5 rows")
        print(df.head())

        print("Missing_values")
        print(df.isnull().sum())

        print("Duplicated rows")
        print(df.duplicated().sum())

        print("Basic statistics")
        print(df.describe())
    except Exception as e:
        print(f"Oops!,i could not load the dataset, here's the exception,{e}")

def main():
    print("Hello, i am DARA your Data Assistant")
    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["bye", "quit", "exit"]:
            print("Goodbye!")
            break
        elif user_input == "upload_dataset":
            print("Please enter the file path the dataset here:")
            file_path = input("You: ").strip().strip("\"")
            load_dataset(file_path)
        else:
            print("Please enter the file path to begin working with your data.")

if __name__ == "__main__":
    main()



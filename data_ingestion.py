import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

csv_files = list(data_path.glob("*.csv"))

for file_path in csv_files:
    print("-"*30, end=' ')
    print(file_path.name, end=' ')
    print("-"*30)

    try:
        df = pd.read_csv(file_path)

        print("Shape: ", df.shape)
        print("Dtypes:\n", df.dtypes)
        print("Head\n",df.head())
        print("Missing Values:")
        print(df.isnull().sum())
    except Exception as e:
        print(f"Error reading {file_path.name}: {e}")

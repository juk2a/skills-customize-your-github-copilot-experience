# Starter Code: Cleaning Messy Data with Python
import pandas as pd

# 1. Load and inspect the dataset
df = pd.read_csv("sales-messy.csv")
print("Preview:")
print(df.head())
print("\nRows and columns:", df.shape)
print("\nMissing values in each column:")
print(df.isna().sum())

rows_before = len(df)

# 2. Remove duplicate rows
# TODO: Remove duplicate rows from df

# 3. Remove incomplete rows
# TODO: Remove rows that have one or more missing values

# 4. Standardize product names
# TODO: Strip extra spaces and capitalize product names consistently

# 5. Save and check the cleaned dataset
df.to_csv("sales-clean.csv", index=False)
print("\nRows before cleaning:", rows_before)
print("Rows after cleaning:", len(df))
print("Missing values after cleaning:")
print(df.isna().sum())
print("Duplicate rows after cleaning:", df.duplicated().sum())

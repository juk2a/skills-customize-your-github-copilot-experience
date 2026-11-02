# 📘 Assignment: Cleaning Messy Data with Python

## 🎯 Objective

Use Python and pandas to inspect a small sales dataset, fix common data-quality problems, and save a clean version for later analysis.

## 📝 Tasks

### 🛠️ Inspect the Dataset

#### Description
Load the provided CSV file and find out what needs cleaning before the data can be used.

#### Requirements
Completed program should:

- Load `sales-messy.csv` into a pandas DataFrame
- Display a preview and the number of rows and columns
- Check for missing values in each column

### 🛠️ Clean the Data

#### Description
Remove repeated or incomplete records and make product names consistent, even when capitalization or extra spaces differ.

#### Requirements
Completed program should:

- Remove duplicate rows
- Remove rows that have missing values
- Remove extra spaces from product names and use consistent capitalization

### 🛠️ Save and Summarize

#### Description
Save the cleaned dataset and report how many rows were removed during cleaning.

#### Requirements
Completed program should:

- Save the result as `sales-clean.csv` without adding a DataFrame index column
- Print the number of rows before and after cleaning
- Confirm that the cleaned data has no missing values or duplicate rows

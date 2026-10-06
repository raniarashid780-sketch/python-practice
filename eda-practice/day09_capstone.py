# Dataset: your messy Kaggle dataset (cafe sales data + https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training )

from pathlib import Path
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Task 1: First look
# - Print shape, columns, dtypes, missing counts
# - Predict before coding: which columns will be the messiest, and why?

csv_path = Path(__file__).with_name("dirty_cafe_sales.csv")
df = pd.read_csv(csv_path)
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data Types:")
print(df.dtypes)
print("Missing Values:")
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

print("Value Counts:")
print(df.value_counts("Item"))
print(df.value_counts("Payment Method"))
print(df.value_counts("Location"))

print("Summary Statistics:")
print(df.describe(include="all"))
print(df.groupby('Item')['Price Per Unit'].unique())
raw = df.copy()

num_cols = ['Quantity', 'Price Per Unit', 'Total Spent']

for col in num_cols:
    before = df[col].isna().sum()
    df[col] = pd.to_numeric(df[col], errors='coerce')
    after = df[col].isna().sum()
    print(col, 'NaN before:', before, '-> after:', after)

print("After conversion to numeric:")
print(df[num_cols].describe())
print(df.dtypes)

print("Total Spent == Quantity * Price Per Unit:", (df['Total Spent'] == df['Quantity'] * df['Price Per Unit']).all())
complete = df.dropna(subset=['Quantity', 'Price Per Unit', 'Total Spent'])
match = np.isclose(complete['Total Spent'],
                   complete['Quantity'] * complete['Price Per Unit'])
print('complete rows:', len(complete))
print('rows that match:', match.sum())
print('mismatches:', (~match).sum())

# Task 2: Clean it
# - Handle missing values, duplicates, wrong types
# - Keep a "cleaning log": one comment line per decision, with the reason

menu = {
    "Cake": 3.0,
    "Coffee": 2.0,
    "Cookie": 1.0,
    "Salad": 5.0,
    "Sandwich": 4.0,
    "Smoothie": 4.0,
    "Juice": 3.0,
    "Tea": 1.5
}
df["Price Per Unit"] = df["Price Per Unit"].fillna(df["Item"].map(menu))
print("Price Per Unit missing after fillna:", df["Price Per Unit"].isna().sum())

# Case 1: Total missing, Quantity and Price present
mask = df['Total Spent'].isna() & df['Quantity'].notna() & df['Price Per Unit'].notna()
print('rows fixable (Total):', mask.sum())
df.loc[mask, 'Total Spent'] = df.loc[mask, 'Quantity'] * df.loc[mask, 'Price Per Unit']

# Case 2: Quantity missing, Total and Price present
mask = df['Quantity'].isna() & df['Total Spent'].notna() & df['Price Per Unit'].notna()
print('rows fixable (Quantity):', mask.sum())
df.loc[mask, 'Quantity'] = df.loc[mask, 'Total Spent'] / df.loc[mask, 'Price Per Unit']

q = df['Quantity']
bad = q.notna() & ((q % 1 != 0) | (q < 1) | (q > 5))
print('bad Quantity values:', bad.sum())

# Case 3: Price Per Unit missing, Total and Quantity present
mask = df['Price Per Unit'].isna() & df['Total Spent'].notna() & df['Quantity'].notna()
print('rows fixable (Price Per Unit):', mask.sum())
df.loc[mask, 'Price Per Unit'] = df.loc[mask, 'Total Spent'] / df.loc[mask, 'Quantity']

core = ['Quantity', 'Price Per Unit', 'Total Spent']
print('rows still missing at least one:', df[core].isna().any(axis=1).sum())

complete = df.dropna(subset=core)
print('mismatches after repair:', (~np.isclose(complete['Total Spent'], complete['Quantity'] * complete['Price Per Unit'])).sum())

left = df[df[core].isna().any(axis=1)]
print(len(left))
print(left[core + ['Item']].isna().sum())

text_cols = ['Item', 'Payment Method', 'Location']
df[text_cols] = df[text_cols].replace(['UNKNOWN', 'ERROR'], np.nan)
print(df[text_cols].isna().sum())

df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')
print('bad dates:', df['Transaction Date'].isna().sum())

# LOG: Price Per Unit filled from Item menu (each real item has exactly one price) -> X rows recovered
# LOG: Quantity values cleaned (must be integers between 1 and 5) -> X rows cleaned
# LOG: Transaction Date coerced to datetime -> X rows with bad dates

# Task 3: Look for patterns
# - Check outliers and distributions of the numeric columns
# - Pick 3 charts, each with a one-line reason for choosing that chart type

# Task 4: Feature-signal check (same method as Day 8)
# - Choose the target column you want to predict, with the question in one sentence
# - Compare each feature against it with groupby + mean + count
# - Mark each feature: keep / drop / duplicate / leakage risk
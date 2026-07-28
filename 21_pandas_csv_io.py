"""Day 2: Pandas CSV I/O."""
import pandas as pd

df = pd.read_csv("sample_sales.csv")

# Prediction: head() shows first 5 rows, unformatted by my expectations of order
print(df.head())
print(df.head(2))

df.info()

print(df.describe())
print(df.describe(include="all"))

df.to_csv("output.csv", index=False)
reloaded_df = pd.read_csv("output.csv")
print(df.equals(reloaded_df))

print(pd.__version__)
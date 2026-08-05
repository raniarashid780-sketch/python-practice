"""Day 5: Pandas missing data handling """
import numpy as np
import pandas as pd
sample_data = pd.DataFrame({
    "Order_ID":["A-1042", "B-2087", "C-3114", "D-4201", "E-5126","F-6359"],
    "Department":["Electronics", "Home", "Sports", pd.NA, "Home", "Sports"],
    "Revenue":[1250.5, 980.0, np.nan, 300.75, 1300.50, 500.25],
    "Region":["North", "South", "East", "West", "North", "West"]
})
# we are using numpy here because if we give an empty value as pd.NA in the Revenue column pandas will mark the column dtype as object so we are using numpy's empty value.
print(sample_data.dtypes)
print(sample_data.isna().sum())
print(sample_data.dropna())
print(sample_data.dropna(subset=["Revenue"]))
sample_data["Revenue"] = sample_data["Revenue"].fillna(sample_data["Revenue"].mean())
# statistical fill — more defensible than a hardcoded 0
sample_data["Department"] = sample_data["Department"].fillna("Unknown")
print(sample_data)
print(sample_data.isna().sum())
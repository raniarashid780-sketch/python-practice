"""Day 8: pandas sorting, ranking, and value counts."""
import pandas as pd
sample_data = pd.DataFrame({
    "Order_ID":["A-1042", "B-2087", "C-3114", "D-4201", "E-5126","F-6359", "G-9234", "H-1543"],
    "Department":["Electronics", "Home", "Sports", "Electronics", "Home", "Sports", "Electronics", "Home"],
    "Revenue":[1250.5, 980.0, 800.0, 300.75, 1300.50, 500.25, 800.0, 2000.50],
    "Region":["North", "South", "East", "West", "North", "West", "East", "South"]
})
print(sample_data.sort_values("Revenue"))
print(sample_data.sort_values("Revenue", ascending=False,inplace=True))
sample_data.sort_values(["Department","Revenue"])
print(sample_data)
sample_data.sort_index(inplace=True)
print(sample_data)
print(sample_data["Revenue"].rank())
#
print(sample_data["Revenue"].value_counts(normalize=True))
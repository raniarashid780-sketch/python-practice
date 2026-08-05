"""Day 6: Pandas Groupby"""
import pandas as pd
sample_data = pd.DataFrame({
    "Order_ID":["A-1042", "B-2087", "C-3114", "D-4201", "E-5126","F-6359"],
    "Department":["Electronics", "Home", "Sports", "Electronics", "Home", "Sports"],
    "Revenue":[1250.5, 980.0, 800.0, 300.75, 1300.50, 500.25],
    "Region":["North", "South", "East", "West", "North", "West"]
})
print(sample_data["Department"])
print(sample_data.groupby("Department")["Revenue"].sum())
print(sample_data.groupby("Department")["Revenue"].agg(["sum","mean","count"]))
grouped = sample_data.groupby(["Department", "Region"])["Revenue"].sum()
print(grouped)          # before reset — Department & Region form a MultiIndex, no separate integer index
print(grouped.reset_index())   # after reset — Department & Region become normal columns, default 0..n index added
print(sample_data.groupby("Department"))
# groupby() alone only builds the group structure lazily — no aggregation is
# computed or displayed until a method like .sum() is called on it
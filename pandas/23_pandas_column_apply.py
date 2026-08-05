"""Day 4:Pandas column operations and apply """
import pandas as pd
sample_data = pd.DataFrame({
    "Order_ID":["A-1042", "B-2087", "C-3114", "D-4201", "E-5126","F-6359"],
    "Department":["Electronics", "Home", "Sports", "Electronics", "Home", "Sports"],
    "Revenue":[1250.5, 980.0, 2140.75, 300.75, 1300.50, 500.25],
    "Region":["North", "South", "East", "West", "North", "West"]
})
print(sample_data)
sample_data["Revenue_with_tax"] = sample_data["Revenue"] * 1.15
print(sample_data)
def tag_high_value(revenue):
    return "High" if revenue > 1000 else "Low"
# this funstion goes through all values of the column and check condition and return the corresponding valus based on values
sample_data["Value_tag"] = sample_data["Revenue"].apply(tag_high_value)
print(sample_data)
def flag_value(row):
    return row["Revenue"] > 1000 and row["Department"] == "Electronics"
sample_data["Flagged"] = sample_data.apply(flag_value, axis=1)
print(sample_data)
sample_data = sample_data.drop("Region", axis=1)
sample_data.drop("Order_ID", axis=1, inplace=True)
print(sample_data)
print(sample_data.dtypes)
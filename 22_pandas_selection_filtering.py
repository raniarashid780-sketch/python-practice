"""Day 3: Pandas selection and filtering"""
import pandas as pd
sample_data = pd.DataFrame({
    "Order_ID":["A-1042", "B-2087", "C-3114", "D-4201", "E-5126","F-6359"],
    "Department":["Electronics", "Home", "Sports", "Electronics", "Home", "Sports"],
    "Revenue":[1250.5, 980.0, 2140.75, 300.75, 1300.50, 500.25],
    "Region":["North", "South", "East", "West", "North", "West"]
})
print(type(sample_data["Order_ID"]))
print(type(sample_data.Order_ID))
print(sample_data[["Department", "Revenue"]])
print(sample_data.loc[0:2])
# Inclusive slicing is label based slicing it prints all the rows including the end point unlike lists
print(sample_data.iloc[0:2])
# Exclusive slicing is index based slicing it prints the rows but excludes the endpoint like lists
mask = sample_data["Revenue"]>1000.00
print(sample_data[mask])
# you can also  do it in one line like this
print(sample_data[sample_data["Revenue"]>1000.00])
print(sample_data[(sample_data["Revenue"]>800.00) & (sample_data["Department"]=="Electronics")])
print(sample_data.loc[sample_data["Revenue"]>800.00 ,"Region"])
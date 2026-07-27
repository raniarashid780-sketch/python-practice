"""Day 2: Pandas CSV I/O"""
import pandas as pd
df = pd.read_csv("sample_sales.csv")
# By default head gives data on first five rows
print(df.head())
# it will show the top 2 rows index starts from 0 so it will show rows 0 and 1
print(df.head(2))
# it will  show the full information about data
df.info()
# It will provide the mean, std, min, max etc of all data
# by default it gives data on just numeric values
print(df.describe())
# if you include all it will give data on all datatypes
print(df.describe(include="all"))
df.to_csv("output.csv", index=False)
df2 = pd.read_csv("output.csv")
print(df.equals(df2))



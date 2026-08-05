"""Day 1:Pandas series and DataFrame """
import pandas as pd
s = pd.Series([100, 200, 300], index=("a","b","c"))
print(s)
df = pd.DataFrame({
    "Product":["Charger", "Cable", "Cover"],
    "Sales":[200, 400, 350]
})
print(df)
print(df.shape)
print(df.dtypes)
# In a data frame a column can have its own data type like in our example products column has str datatype and sales column has int64 datatype
print(df.loc[0])
print(df.iloc[0])
# .loc access the data by label and .iloc access data purely by its position/index
# if you know the name of column or label on it use .loc and if you know the index use .iloc
col = df["Sales"]
print(type(col))
# in pandas data frame is just series glued together when we access a column it is just a series
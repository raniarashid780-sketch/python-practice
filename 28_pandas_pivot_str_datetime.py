"""Day 9: Pandas pivot, string, and datetime operations."""
import pandas as pd
sales_data = pd.DataFrame({
    "Department": [
        "Electronics", "Furniture", "Books", "Home",
        "Electronics", "Furniture", "Books", "Home",
    ],
    "Region": [
        "North", "South", "East", "West",
        "West", "North", "South", "East",
    ],
    "Revenue": [1200, 800, 300, 450, 950, 700, 220, 600],
    "Ship_Date": [
        "2024-01-15", "2024-01-16", "2024-01-17", "2024-01-18",
        "2024-01-20", "2024-01-21", "2024-01-22", "2024-01-23",
    ],

})
# Replace the current Tags column with list values.
sales_data["Tags"] = [
    ["Sale", "Electronics"],
    ["New", "Home"],
    ["Sale", "Furniture"],
    ["New", "Electronics"],
    ["Sale", "Books"],
    ["New", "Home"],
    ["Sale", "Electronics"],
    ["Discount"],
]
print(sales_data.pivot_table(values="Revenue", index="Department", columns="Region", aggfunc="sum", fill_value=0))
# groupby summarizes rows; pivot_table reshapes that summary into a neat table.
print(sales_data["Department"].str.upper())
print(sales_data["Department"].str.contains("Elec"))
print(sales_data.dtypes)
sales_data["Ship_Date"] = pd.to_datetime(sales_data["Ship_Date"])
print(sales_data.dtypes)
print(sales_data["Ship_Date"].dt.year) # prints year
print(sales_data["Ship_Date"].dt.month) # prints month number
print(sales_data["Ship_Date"].dt.month_name()) # prints month name
print(sales_data["Ship_Date"].dt.day_name()) #prints day name
sales_data["Ship_Month"] = sales_data["Ship_Date"].dt.month
sales_data["Ship_Day_Name"] = sales_data["Ship_Date"].dt.day_name()
print(sales_data)
print(len(sales_data))       # 8 rows
exploded_data = sales_data.explode("Tags")
print(len(exploded_data))    # -> however many, since some orders had 2 tags, one had 1
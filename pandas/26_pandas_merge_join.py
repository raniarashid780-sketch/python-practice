"""Day 7: Pandas merge and join."""

import pandas as pd

orders_df = pd.DataFrame({
    "Order_ID": [101, 102, 103, 104],
    "Department": ["Electronics", "Furniture", "Books", "Home"],
    "Revenue": [1200, 800, 150, 600],
})

shipping_df = pd.DataFrame({
    "Order_ID": [102, 103, 105],
    "Ship_Date": ["2024-01-02", "2024-01-03", "2024-01-04"],
    "Status": ["Shipped", "Delivered", "Pending"],
})
print(pd.merge(orders_df, shipping_df, on="Order_ID", how="inner"))
print(pd.merge(orders_df, shipping_df, on="Order_ID", how="left"))
print(pd.merge(orders_df, shipping_df, on="Order_ID", how="outer"))
more_orders_df = pd.DataFrame({
    "Order_ID": [106, 107],
    "Department": ["Sports", "Toys"],
    "Revenue": [450, 220],
})
print(pd.concat([orders_df, more_orders_df]))

# merge combines dataframes based on a shared key across different information;
# concat stacks dataframes with the same structure, no key matching involved
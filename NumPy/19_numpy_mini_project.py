"""Day 9: Mini project using the concepts I have learned so far """
import numpy as np
np.random.seed(500000)
# reproducible integers between 1 and 50000
sales = np.random.randint(1, 50001, size=35)
# assign reshaped array back to sales
sales = sales.reshape(7, 5)
avg = sales.mean()
mask2 = sales < avg
below_avg = sales[mask2]

mask = sales > avg
above_avg = sales[mask]
sales_per_product = sales.sum(axis=0)
max_sale = sales_per_product.max()
top_product_index = sales_per_product.argmax()
print("Sales Data")
print(sales)
print(f"Overall average: {sales.mean()} ")
print(f"Sales below average: {below_avg}")
print(f"Sales above average: {above_avg}")
print(f"Total sales per product: {sales_per_product}")
print(f"Top selling product: Product {top_product_index + 1}, total sales = {sales_per_product[top_product_index]}")

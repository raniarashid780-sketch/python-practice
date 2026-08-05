"""Day 2: matplotlib bar charts, scatter plots, and histograms."""
import numpy as np
import matplotlib.pyplot as plt
# Bar chart — Department is a discrete category, not a continuous number,
# so bars compare totals across named groups rather than showing a trend
departments = ["Electronics", "Home", "Sports", "Furniture"]
revenue = [16500, 1300, 9000, 2700]
fig, ax = plt.subplots()
ax.bar(departments, revenue)
ax.set_xlabel("Department")
ax.set_ylabel("Revenue")
ax.set_title("Total Revenue by Department")
plt.show()
# Scatter Chart — Scatter charts are used to show the relationship between two continuous variables.
#  Each point represents an observation in the dataset, with its position determined by the values of the two variables.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2, 5, 7, 9, 11, 13, 15, 17, 19, 21])
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Scatter plot of Y ~ 2x (with small variation)")
plt.show()
# Histogram — Histograms are used to visualize the distribution of a single continuous variable.
heights_in_inches = [
    68.7, 66.5, 69.2, 72.3, 66.1, 66.1, 72.5, 69.6, 65.3, 68.9,
    65.3, 65.3, 67.8, 60.2, 60.8, 64.9, 63.3, 68.0, 63.7, 61.9,
    72.1, 66.1, 67.2, 61.9, 65.0, 67.3, 62.8, 68.3, 64.8, 65.9
]
fig, ax = plt.subplots()
ax.hist(heights_in_inches, bins=10)
ax.set_xlabel("Height")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Heights")
plt.show()
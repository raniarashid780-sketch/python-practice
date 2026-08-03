"""Day 4: matplotlib subplots — multiple charts in one figure."""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 3, 5, 7]

categories = ["A", "B", "C", "D"]
values = [4, 2, 6, 3]

x2 = [1, 2, 3, 4, 5]
y2 = [3, 5, 2, 4, 6]

data = [1, 2, 2, 3, 4, 4, 5, 3, 2, 1]

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

axes[0, 0].plot(x, y1, color="tab:blue")
axes[0, 0].set_xlabel("X values")
axes[0, 0].set_ylabel("Y values")
axes[0, 0].set_title("Line chart")

axes[0, 1].bar(categories, values, color="tab:orange")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Value")
axes[0, 1].set_title("Bar chart")

axes[1, 0].scatter(x2, y2, color="tab:green")
axes[1, 0].set_xlabel("X values")
axes[1, 0].set_ylabel("Y values")
axes[1, 0].set_title("Scatter chart")

axes[1, 1].hist(data, bins=5, color="tab:red")
axes[1, 1].set_xlabel("Value")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].set_title("Histogram")

fig.suptitle("Four charts on one page", fontsize=16)
fig.tight_layout()
# axes is a 2D NumPy array of shape (2, 2) here since nrows=2, ncols=2 —
# indexed with [row, col]; a single-row/column grid would instead give a
# 1D array indexed with just axes[i]
plt.show()
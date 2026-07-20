"""Day 5: NumPy aggregations """
import numpy as np
a = np.arange(12).reshape(3, 4)
print(a)
print(a.sum())  # Sum of all elements
print(a.min())  # Minimum element
print(a.max())  # Maximum element
print(a.mean())  # Mean of all elements
print(a.std())  # Standard deviation
print(a.sum(axis=0))  # [12,15,18,21], shape (4,) — collapses rows (axis 0), one value per column
print(a.sum(axis=1))  # [6,22,38], shape (3,) — collapses columns (axis 1), one value per row
a = np.array([1, 2, 3, 4])

print(a.sum())       # 10 — one number, everything added together
print(np.cumsum(a))   # [1, 3, 6, 10] — running total at each step
# difference between sum and cumsum is that sum gives you the total of all elements in the array,
# while cumsum gives you the cumulative sum at each index, so you can see how the total builds up as you go through the array.
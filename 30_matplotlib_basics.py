"""Day 1: matplotlib figure and axes basics."""
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
b = np.array([8, 10, 14, 20, 27, 33, 36, 35, 30, 22, 14, 9])
ax.plot(a, b)
ax.set_xlabel("Month")
ax.set_ylabel("Temperature")
ax.set_title("Weather in DG khan")
plt.show()
# Figure is the entire sheet of paper, it is the blank canvas itself while axis is the individual plot with actual x and y lines
# one figure can have many axes but each axis exactly belongs to one figure
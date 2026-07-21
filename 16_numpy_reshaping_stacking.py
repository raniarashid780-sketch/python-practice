"""Day 6: Numpy reshaping and stacking."""
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.vstack((a, b)))  #Vertical stack
# the shape of the result is (2, 3) because we stacked two 1D arrays vertically, resulting in a 2D array with 2 rows and 3 columns.
print(np.hstack((a, b)))  # Horizontal stack
# the shape of the result is (6,) because we stacked two 1D arrays horizontally, resulting in a 1D array with 6 elements.
grid = np.array([[1, 2, 3], [4, 5, 6]])
print(grid.flatten())  # Flatten the 2D array into a 1D array
print(grid.ravel())  # Another way to flatten the array
# the difference between flatten and ravel is that flatten returns a copy of the array, while ravel returns a view of the array whenever possible.
# This means that modifying the result of ravel may affect the original array, while modifying the result of flatten will not.
print(np.split(np.arange(12), 4))  # Split an array of 12 elements into 4 equal parts

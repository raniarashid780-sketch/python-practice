"""Day 4: NumPy broadcasting """
import numpy as np
a = np.array([1,2,3,4,5])
print(a + 10) # broadcasting, adds 10 to each element of a
grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row = np.array([1, 0, 1])
print(grid + row)
#grid is (3,3), row is (3,) → padded to (1,3) → last dim 3=3, first dim 3 vs 1 → the row dimension (axis 0) is what stretches, because that's where the 1 is.
grid2 = np.array([[1, 2, 3], [2, 2, 2], [3, 3, 3]])
row2 = np.array([[1], [0], [1]])
print(grid2 + row2)
#grid2: (3, 3) row2:  (3, 1) so the last dimension is 3 vs 1, the first dimension is 3 vs 3 → the row dimension (axis 1) is what stretches, because that's where the 1 is.
grid3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
row3 = np.array([[1, 4, 3, 4], [0, 5, 6, 7], [1, 8, 9, 10]])
print(grid3 + row3)# it will give value error
# just like this (ValueError: operands could not be broadcast together with shapes (4,3) (3,4))
# because the shapes of 2 arrys are not comaptible for broadcasting, the first array has shape (4,3) and the second array has shape (3,4)


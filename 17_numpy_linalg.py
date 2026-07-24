"""Day 7: NumPy linear algebra."""
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a @ b)  # Matrix multiplication
# the @ operator is used for matrix multiplication in NumPy. It performs the dot product of two arrays.
# In this case, it multiplies the 2x2 matrix a with the 2x2 matrix b, resulting in another 2x2 matrix.
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c)
print(c.T)  # Transpose of c
# when we take transpose of a matrix, we flip it over its diagonal, turning its rows into columns and its columns into rows.
# in this case the shape of c was (2,3) when we took its transpose it became (3,2)
d = np.array([[1, 0], [0, 1]])
print(np.linalg.det(d))
print(np.linalg.inv(d))


"""Day 7: NumPy linear algebra."""
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
# manual: row0·col0 = 1*5+2*7=19, row0·col1 = 1*6+2*8=22
#         row1·col0 = 3*5+4*7=43, row1·col1 = 3*6+4*8=50
# expected: [[19,22],[43,50]]
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
d = np.array([[4, 7], [2, 6]])
print(np.linalg.det(d))    # should be 4*6 - 7*2 = 10
d_inv = np.linalg.inv(d)
print(d_inv)
print(d @ d_inv)   # should be ~[[1,0],[0,1]], but likely shows tiny values like 1.11e-16 instead of exact 0
# floating point can't represent all decimal fractions exactly in binary,
# so the "zero" entries often come out as something like 1e-17 instead of a clean 0

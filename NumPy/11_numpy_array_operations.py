"""Day 3: NumPy array operations, broadcasting, and universal functions."""
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
print(a + b)  # Element-wise addition
print(a * b)  # Element-wise multiplication
# it's not matrix multiplication, its element wise multiplication
# because numpy multiplies them as [0] of a with [0] of b, [1] of a with [1] of b and so on
print(a - b)  # Element-wise subtraction
print(a / b)  # Element-wise division
print(np.sqrt(a))  # Square root of each element in a
print(np.exp(a))  # Exponential of each element in a
print(np.abs(-a))  # Absolute value of each element in a
print(a > b)  # Element-wise comparison
print(a == b)  # Element-wise equality check
# we got all false in comparison and equality check because all elements of a are less than b, so all comparisons return false
mask = a > 3
print(mask)        # boolean array
print(a[mask])      # actually filter a using the mask
print(np.dot(a, b))  #Dot product of a and b
# dot product is the sum of the products of the corresponding entries of the two sequences of numbers.
#In this case, it will be 1*10 + 2*20 + 3*30 + 4*40 + 5*50 = 550
"""Day 2: NumPy indexing, slicing, view vs copy, boolean masking, and reshape."""
import numpy as np 
nums = np.array([1, 2, 3, 4, 5])
print(nums[0])  # Access the first element
print(nums[2])  # Access the third element
print(nums[-1])  # Access the last element
grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(grid)
print(grid[1, 2])  # Access the element in the second row, third column
print(nums[2:5])
nums[2:5] = 10, 12, 13
print(nums) 
# in numpy slicing returns a view of the original array, not a copy. 
#So if you modify the slice, it will modify the original array as well.

view = nums[2:5]          # a VIEW — same memory as nums
view[0] = 999
print(nums)                 # changed — proves it's a view

real_copy = nums[2:5].copy()   # an actual COPY — separate memory
real_copy[0] = -1
print(nums)                     # unchanged — proves it's independent
print(real_copy)

print(grid[grid > 5])  # This will print elements of the grid that are greater than 5
reshaped_arr = np.arange(12).reshape(3, 4)
print(reshaped_arr)
print(reshaped_arr[1:3, 1:3])  # This will print a slice of the array

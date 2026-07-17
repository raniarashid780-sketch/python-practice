import numpy as np 

evens=np.arange(2,22,2)

print(evens)
zeros_grid=np.zeros((3,3))
print(zeros_grid)
print(zeros_grid.dtype)
ones_grid=np.ones((3,3))
print(ones_grid)
print(ones_grid.dtype)

numeric_upcast_test = np.array([1, 2, 3.7])
print(numeric_upcast_test.dtype)  # float64
# int and float mix → int loses no precision when promoted to float,
# so NumPy silently upcasts the whole array to float64
linspace_vals=np.linspace(-1,1,7)
print(linspace_vals)
print(linspace_vals.shape)
print(linspace_vals.size)
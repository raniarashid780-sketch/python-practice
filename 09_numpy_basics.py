import numpy as np 

array=np.arange(2,22,2)

print(array)
array2=np.zeros((3,3))
print(array2)
print(array2.dtype)
array3=np.ones((3,3))
print(array3)
print(array3.dtype)
array4=np.array([1,"2",3])
print(array4.dtype)
#no lossless numeric type covers a string, so it falls back to text
array5=np.linspace(-1,1,7)
print(array5)
print(array5.shape)
print(array5.size)
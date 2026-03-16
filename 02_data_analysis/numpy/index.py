import numpy as np

arr = np.array([[3, 4, 5, 1, 2], [6, 7, 8, 9, 10]])



# print(arr)
################# Most Important Attributes of that Np Arrays ########################
# print("Dimension", arr.ndim)
# print("Array Shape", arr.shape)
# print("Array size", arr.size)
# print("Array item size", arr.itemsize)
# print("Array Nbytes Size", arr.nbytes)
# print("Transpose of that array", arr.T)
# print("Array type", arr.dtype)


# This is method of the array

# print(arr.reshape(2, 4, 3))
# print(arr.flatten())
# print(arr.sum())
# print(arr.mean())
# print(arr.max())
# print(arr.sort())
# print(arr.copy())
# print(arr.astype(str))
# print(arr.transpose())


# mArr = np.arange(1, 10, 2, float)
# mArr = np.linspace(1, 50, num=50, endpoint=True, dtype=int)
# mArr = np.zeros(2)
# mArr = np.zeros((2, 4, 5))    
# print(mArr)
# mArr = np.ones((2, 4, 5))
print(np.sum([1, 2, 3]))
print(np.mean([1, 2, 3]))
print(np.min([1, 2, 3]))
print(np.max([1, 2, 3]))
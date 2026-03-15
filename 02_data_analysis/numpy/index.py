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

# print(arr.reshape(2, 4, 3))
# print(arr.flatten())
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.sort())
print(arr.copy())
print(arr.astype(str))
print(arr.transpose())

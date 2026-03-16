import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
max_index = arr.argmax()
arr[max_index] = 0
print(arr)
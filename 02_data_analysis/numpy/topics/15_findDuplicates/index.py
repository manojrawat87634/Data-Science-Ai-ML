import numpy as np

arr = np.array([1,2,3,2,4,5,1,6])

values, counts = np.unique(arr, return_counts=True)

duplicates = values[counts > 1]

print(duplicates)
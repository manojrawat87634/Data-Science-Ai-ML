import numpy as np

arr = np.array([2, 5, 8, 12, 15])
target = 10

closest = arr[np.abs(arr - target).argmin()]

print(closest)
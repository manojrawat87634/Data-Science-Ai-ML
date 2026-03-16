import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

flat = arr.flatten()
reshaped = flat.reshape(3,2)

print("Flatten:", flat)
print("Reshaped:\n", reshaped)
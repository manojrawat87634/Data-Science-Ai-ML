import numpy as np

arr = np.array([
    [3, 4, 5],
    [10, 2, 1],
    [6, 7, 8]
])

row_sums = arr.sum(axis=1)      # sum of each row
max_row_index = np.argmax(row_sums)

print("Row sums:", row_sums)
print("Row with max sum:", max_row_index)
print("Maximum sum:", row_sums[max_row_index])
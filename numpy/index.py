import numpy as np

# Creating
a = np.array([[1, 2, 3], [4, 5, 6], [4, 3, 5]])
# # Shape Method give the row * col
# print(a.shape)


# # Slicing in numpy
# print(a[0])
# print(a[:, 0])

# # Boolean masking (a[a > 0])
# r = np.array([10, 11, 13, 14, 15])
# n_r = r[r % 2 == 0]
# print("--- Even Numbers ----")
# print(n_r)
# print("-------")
data = np.array([
    [25, 50000],
    [30, 60000],
    # [22, 30000],
    # [35, 80000]
])

print(data.mean())
print(data.sum())
print(data.std())


n_arr = (data + 10)
print(n_arr)

a = data @ data
print(a)

# high_salary = data[data[:, 1] > 50000]
# print(high_salary)

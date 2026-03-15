import numpy as np

# Create arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3],
              [4, 5, 6]])

# Basic operations
add = a + 10
mul = a * 2

# Reshaping
c = np.arange(1, 13)
c_reshaped = c.reshape(3, 4)

# Broadcasting
d = c_reshaped + np.array([1, 2, 3, 4])

# Slicing
slice_a = a[1:4]
slice_b = b[:, 1:]

# Aggregations
total_sum = np.sum(c_reshaped)
row_mean = np.mean(c_reshaped, axis=1)

# Matrix operations
x = np.array([[1, 2],
              [3, 4]])
y = np.array([[5, 6],
              [7, 8]])

dot_product = np.dot(x, y)
transpose = x.T
inverse = np.linalg.inv(x)
determinant = np.linalg.det(x)

# Random numbers
rand_matrix = np.random.rand(3, 3)
normal_matrix = np.random.randn(3, 3)

# Boolean masking
mask = a > 3
filtered = a[mask]

# Print results
print("a:", a)
print("b:\n", b)
print("add:", add)
print("mul:", mul)
print("c:\n", c)
print("reshaped c:\n", c_reshaped)
print("broadcast result:\n", d)
print("slice a:", slice_a)
print("slice b:\n", slice_b)
print("total sum:", total_sum)
print("row mean:", row_mean)
print("dot product:\n", dot_product)
print("transpose:\n", transpose)
print("inverse:\n", inverse)
print("determinant:", determinant)
print("random matrix:\n", rand_matrix)
print("normal matrix:\n", normal_matrix)
print("filtered:", filtered)

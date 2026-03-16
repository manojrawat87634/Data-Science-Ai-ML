import numpy as np


arr = np.array([12, 34, 56, 76, 8, 90])
nArr = (arr - arr.min() )/ (arr.max() - arr.min())

print(nArr)
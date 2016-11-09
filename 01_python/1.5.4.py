# numpyのN次元配列

import numpy as np

x = np.array([[1, 2], [3, 4]])
print(x)
# [[1 2]
#  [3 4]]

print(x.shape)
# (2, 2)

print(x.dtype)
# int64

y = np.array([[3, 0], [0, 6]])
print(x + y)
#[[ 4  2]
# [ 3 10]]

print(x * y)
#[[ 3  0]
# [ 0 24]]

print(x * 10)
# [[10 20]
#  [30 40]]
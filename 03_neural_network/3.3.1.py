# 多次元配列

import numpy as np

x = np.array([1. ,2. ,3., 4.])
print(x)
# [ 1.  2.  3.  4.]

print(np.ndim(x))
# 1

print(x.shape)
# (4,)

print(x.shape[0])
# 4

y = np.array([[1. ,2.], [3., 4.], [5. ,6.]])
print(y)
# [[ 1.  2.]
#  [ 3.  4.]
#  [ 5.  6.]]

print(np.ndim(y))
# 2

print(y.shape)
# (3, 2)

print(y.shape[0])
# 3
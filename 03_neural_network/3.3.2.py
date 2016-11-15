# 行列の内積

import numpy as np

x = np.array([[1. ,2.], [3., 4.]])
print(x.shape)
# (2, 2)

y = np.array([[5., 6.], [7., 8.]])
print(y.shape)
# (2, 2)

print(np.dot(x, y))
# [[ 19.  24.]
#  [ 43.  50.]]

print(np.dot(y, x))
# [[ 23.  34.]
#  [ 31.  46.]]

x = np.array([[1. ,2., 3.], [4., 5., 6.]])
print(x.shape)
# (2, 3)

y = np.array([[1., 2.], [3., 4.], [5., 6.]])
print(y.shape)
# (3, 2)

print(np.dot(x, y))
# [[ 22.  28.]
#  [ 49.  64.]]

print(np.dot(y, x))
# [[  9.  12.  15.]
#  [ 19.  26.  33.]
#  [ 29.  40.  51.]]

z = np.array([[1., 2.], [3., 4.]])
print(z.shape)
# (2, 2)

# print(np.dot(x, z))
# ValueError: shapes (2,3) and (2,2) not aligned: 3 (dim 1) != 2 (dim 0)

z = np.array([1., 2., 3.])
print(z.shape)
# (3, )

print(np.dot(x, z))
# [ 14. 32.]

# ニューラルネットワークの内積

import numpy as np

x = np.array([1. ,2.])
print(x.shape)
# (2, )

w = np.array([[1., 3., 5.], [2., 4., 6.]])
print(w.shape)
# (2, 3)

y = np.dot(x, w)
print(y)
# [ 5. 11. 17. ]

z = np.dot(w, x)
print(z)
# ValueError: shapes (2,3) and (2,) not aligned: 3 (dim 1) != 2 (dim 0)
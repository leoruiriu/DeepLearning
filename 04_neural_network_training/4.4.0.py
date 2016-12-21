# 勾配

import numpy as np
from function.gradient import numerical_gradient

def function_2(x):
    return np.sum(x**2)

y = numerical_gradient(function_2, np.array([3.0, 4.0]))
print(y) # [ 6.  8.]

y = numerical_gradient(function_2, np.array([0.0, 2.0]))
print(y) # [ 0.  4.]

y = numerical_gradient(function_2, np.array([3.0, 0.0]))
print(y) # [ 6.  0.]
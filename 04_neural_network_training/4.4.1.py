# 勾配法

import numpy as np
from function.gradient import gradient_descent

def function_2(x):
    return np.sum(x**2)

init_x = np.array([-3.0, 4.0])
y = gradient_descent(function_2, init_x=init_x, lr=10.0, step_num=100)
print(y) # [ -2.58983747e+13  -1.29524862e+12]

init_x = np.array([-3.0, 4.0])
z = gradient_descent(function_2, init_x=init_x, lr=1e-10, step_num=100)
print(z) # [-2.99999994  3.99999992]
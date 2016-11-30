# 数値微分の例

import numpy as np
import matplotlib.pylab as plt
from function.diff import numerical_diff

def function_1(x):
    return 0.01*x**2 + 0.1*x # y = 0.01x^2 + 0.1x

def tangent_line(f, x):
    d = numerical_diff(f, x)
    y = f(x) - d*x
    return lambda t: d*t + y

print(numerical_diff(function_1, 5)) # 0.1999999999990898
print(numerical_diff(function_1, 10)) # 0.2999999999986347

x = np.arange(0.0, 20.0, 0.1) # 0.0から20.0まで、0.1刻みのx配列
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()

tf = tangent_line(function_1, 5)
y2 = tf(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()
# 重み(weight)とバイアス(bias)の導入

import numpy as np

x = np.array([0, 1]) # 入力
w = np.array([0.5, 0.5]) # 重み
b = -0.7

print(w*x)
# [ 0.   0.5]

print(np.sum(w*x))
# 0.5

print(np.sum(w*x) + b)
# -0.2
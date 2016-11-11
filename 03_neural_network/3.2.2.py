# ステップ関数の実装

import numpy as np

def step_function(x):
    y = x > 0
    return y.astype(np.int)

x = np.array([-1.0, 1.0, 2.0])
print(x)
# [-1. 1. 2.]

y = x > 0
print(y)
# [False True True]

print(y.astype(np.int))
# [0 1 1]

print(step_function(x))
# [0 1 1]
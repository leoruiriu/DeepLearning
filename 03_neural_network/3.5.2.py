# ソフトマックス関数の実装上の注意

import numpy as np

a = np.array([1010, 1000, 990])
print(np.exp(a) / np.sum(np.exp(a)))
# RuntimeWarning: overflow encountered in exp print(np.exp(a) / np.sum(np.exp(a)))
# [ nan  nan  nan]

c = np.max(a) # 1010
x = a - c
print(x) # [  0 -10 -20]

print(np.exp(x) / np.sum(np.exp(x)))
# [  9.99954600e-01   4.53978686e-05   2.06106005e-09]

def softmax(a):
    x = np.max(a)
    exp_a = np.exp(a - x) # オーバーフロー対策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

print(softmax(a))
# [  9.99954600e-01   4.53978686e-05   2.06106005e-09]
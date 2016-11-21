import numpy as np

def softmax(a):
    x = np.max(a)
    exp_a = np.exp(a - x) # オーバーフロー対策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
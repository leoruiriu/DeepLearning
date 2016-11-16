# 各層における信号伝達の実装

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([1.0 ,0.5])
w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])

print(x.shape) # (2, )
print(w1.shape) # (2, 3)
print(b1.shape) # (3, )

a1 = np.dot(x, w1) + b1
print(a1) # [ 0.3  0.7  1.1]

z1 = sigmoid(a1)
print(z1) # [ 0.57444252  0.66818777  0.75026011]

w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])

print(z1.shape) # (3, )
print(w2.shape) # (3, 2)
print(b2.shape) # (2, )

a2 = np.dot(z1, w2) + b2
print(a2) # [ 0.51615984  1.21402696]

z2 = sigmoid(a2)
print(z2) # [ 0.62624937  0.7710107 ]

def identify_function(x):
    return x

w3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])

a3 = np.dot(z2, w3) + b3
print(a3) # [ 0.31682708  0.69627909]

y = identify_function(a3) # もしくは y = a3
print(y) # [ 0.31682708  0.69627909]
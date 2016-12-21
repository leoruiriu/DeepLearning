# ニューラルネットワークに対する勾配

import numpy as np
from temp.gradient_simplenet import simpleNet
from function.gradient import numerical_gradient

net = simpleNet()
print(net.W) # 重みパラメータ

x = np.array([0.6, 0.9])
p = net.predict(x)
print(p)

print(np.argmax(p)) # 最大値のインデックス

t = np.array([0, 0, 1]) # 正解ラベル
print(net.loss(x, t))

f = lambda W: net.loss(x, t)

dW = numerical_gradient(f, net.W)
print(dW)
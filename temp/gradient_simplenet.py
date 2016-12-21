import sys, os
sys.path.append(os.pardir)
import numpy as np
from function.error import cross_entropy_error
from function.gradient import numerical_gradient
from function.softmax import softmax

class simpleNet:
    def __init__(self):
        self.W = np.random.rand(2, 3) # ガウス分布で初期化

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

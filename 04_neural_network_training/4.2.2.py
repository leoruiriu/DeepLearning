# 交差エントロピー誤差

import numpy as np
from function.error import cross_entropy_error

y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0] # y[2]の確立が最も高い場合
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0] # y[7]の確立が最も高い場合
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] # 2が正解

print(cross_entropy_error(np.array(y1), np.array(t))) # 0.510825457099
print(cross_entropy_error(np.array(y2), np.array(t))) # 2.30258409299
# 重みとバイアスによる実装

import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(AND(0, 0)) # x1=0, x2=0
# 0

print(AND(1, 0)) # x1=1, x2=0
# 0

print(AND(0, 1)) # x1=0, x2=1
# 0

print(AND(1, 1)) # x1=1, x2=1
# 1

# wは入力信号の重要度をコントロール
# バイアスは出力信号が1を出力する度合い(発火のしやすさ)をコントロール

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(NAND(0, 0)) # x1=0, x2=0
# 1

print(NAND(1, 0)) # x1=1, x2=0
# 1

print(NAND(0, 1)) # x1=0, x2=1
# 1

print(NAND(1, 1)) # x1=1, x2=1
# 0

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.4
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(OR(0, 0)) # x1=0, x2=0
# 0

print(OR(1, 0)) # x1=1, x2=0
# 1

print(OR(0, 1)) # x1=0, x2=1
# 1

print(OR(1, 1)) # x1=1, x2=1
# 1
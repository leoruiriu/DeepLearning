# 要素へのアクセス

import numpy as np

x = np.array([[51, 55], [14, 19], [0, 4]])
print(x)
# [[51 55]
#  [14 19]
#  [ 0  4]]

print(x[0])
# [51 55]

print(x[0][1])
# 55

for row in x:
    print(row)
    # [51 55]
    # [14 19]
    # [0 4]

x = x.flatten() # xを1次元配列に変換
print(x)
# [51 55 14 19  0  4]

print(x[np.array([0, 2, 4])]) # インデックスが0、2、4番目の要素を取得
# [51 14  0]

print(x < 15) # xの要素の中で15未満の場合True、以外はFalse
# [False False  True False  True  True]

print(x[x>=15]) # 15以上の要素だけの配列を取得
# [51 55 19]
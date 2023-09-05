# simple moving average
# 簡單移動平均

# 均線的意義
# 過濾雜訊->濾波功能
# 平滑功能
# 使用卷積函數計算均線
# np.convolve (卷積)

import sys
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

N = int(input("average period:"))
weights = np.ones(N) / N
print(weights) # [0.2 0.2 0.2 0.2 0.2]
#N = 5 ->

# !!!學用vonvolve 計算均線
c = np.loadtxt('data.csv',dtype='float',delimiter=',',usecols=(6,),unpack=True)
sma = np.convolve(weights,c) #c :close  
#print(sma)
"""
[ 67.22  135.084 204.09  272.954 341.642 343.722 346.234 348.268 351.036
 353.256 355.326 356.786 357.726 358.72  359.472 358.214 354.1   350.644
 346.594 344.566 345.096 347.236 349.136 352.472 354.84  355.27  356.56
 356.63  354.052 352.45  281.378 210.226 139.732  70.398]
"""
sma = sma[N-1:-N+1] # 前面有Ｎ個(N-1) 後面有Ｎ個(-N+1)
t = np.arange(N-1,len(c)) # 時間逐標
print(t)
"""
[ 4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
 28 29]
"""

plot(t,c[N-1:])
plot(t,sma)
show()




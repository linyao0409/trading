# 蒙地卡羅模擬股票價格
# 股價對數常態 左偏
# 指模擬到期末

import math
import numpy as np
import matplotlib.pyplot as plt

S0 = 100.0
T = 1.0
sig = 0.30
r = 0.025
y = 0.02
sig2 = sig*sig

np.random.seed(1234)
VecST = np.array(np.arange(1000))
for i in range(0, 1000):
    ST = S0 * math.exp((r-y-0.5*sig2)*T 
                       + sig*math.sqrt(T)*np.random.standard_normal())
    VecST[i] = ST


plt.figure(figsize=(9, 5))
plt.hist(VecST, bins=50)
plt.grid(True)
plt.xlabel('Price Level')
plt.ylabel('Frequency')
plt.title('Maturity Stock Price Histogram')
plt.show()
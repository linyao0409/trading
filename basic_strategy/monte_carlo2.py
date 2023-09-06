
# 蒙地卡羅模擬股票價格
# 股價對數常態 左偏
# 模擬 路徑

import matplotlib.pyplot as plt
import math
from numpy import *
from time import time

# Parameters
S0 = 100.
K = 105.
T = 1.0
r = 0.05
y = 0.0
sigma = 0.2
M = 50  # 走五十步 （一年有五十週左右）
dt = T / M  # 單位是年
I = 250000  # 模擬的路徑

t0 = time() # 系統時間：想知道模擬花了多久
# Random seed
random.seed(20000)

# Simulating I paths with M time steps
# 這個寫法可以學起來
S = S0 * exp(cumsum(((r-y) - 0.5 * sigma ** 2) * dt
                    + sigma * math.sqrt(dt) * random.standard_normal((M, I)),
                    axis=0))

C0 = math.exp(-r * T) * sum(maximum(S[-1] - K, 0)) / I
print("European Option Value %7.3f" % C0)
t1 = time()
print("Total Time: ", t1-t0)


fst_row = zeros((1, I))
# print(fst_row)
for i in range(0, I):
    fst_row[0, i] = S0
FullS = r_[fst_row, S]

%matplotlib inline

plt.figure(figsize=(9, 6))
plt.plot(FullS[0:50, :100])
plt.grid(True)
plt.xlabel('time step')
plt.ylabel('index level')
plt.title('Simulation Paths')
plt.show()

plt.figure(figsize=(9, 5))
plt.hist(FullS[-1], bins=1000)
plt.grid(True)
plt.xlabel('index level')
plt.ylabel('frequency')
plt.title('Maturity Stock Price Histogram')
plt.show()

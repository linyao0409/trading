# 布林通道 用於反轉策略
import numpy as np
from matplotlib.pyplot import show
from matplotlib.pyplot import plot

# 畫一個在均線上下兩個標準差的線 (不一定是兩個 depend on product)
# 範圍內稱為布林通道

c = np.loadtxt('data.csv',dtype="float",delimiter=",",usecols=(6,),unpack=True)

N = int(input("input the number of weight"))
weights = np.ones(N) / N

sma = np.convolve(weights,c)
sma = sma[N-1:-N+1]
t = np.arange(N-1,len(c))


C = len(c)
deviation = list()

for i in range(N-1,C): #(4~29)
    if i+N < C:
        dev = c[i:i+N]
    else:
        dev = c[-N:]
    
    averages = np.zeros(N)
    averages.fill(sma[i-(N-1)])

    dev = dev - averages
    dev = dev ** 2
    dev = np.sqrt(np.mean(dev))
    deviation.append(dev)

deviation = 2*np.array(deviation)
print(len(deviation),len(sma)) # 26 26
print(deviation)
print(sma)

upperBB = sma + deviation
lowerBB = sma - deviation


c_slice = c[N-1:]
between_bands = np.where((c_slice<upperBB)&(c_slice>lowerBB))

print(between_bands)
#(array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       #17, 18, 19, 20, 21, 22, 23, 25]),)
print(np.ravel(between_bands))
#[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# 25]

n_between_bands = len(np.ravel(between_bands))
print(f"number of close price in bands{n_between_bands}")
#number of close price in bands25

Ratio = n_between_bands / len(c_slice)
print(f"ratio: {Ratio}") #ratio: 0.9615384615384616

plot(t,c[N-1:])
plot(t,sma)
plot(t,upperBB)
plot(t,lowerBB)
show()

"""
使用移动窗口计算标准差的主要原因是在实际应用中，我们通常对价格的短期波动性更感兴趣，而不是整个数据集的波动性。通过使用移动窗口，您可以捕捉到价格的短期变化，从而更准确地构建布林通道，以便用于反转策略。

虽然代码中可能会涉及一些额外的步骤来计算标准差，但这些步骤的目的是确保您正确地捕获价格的波动范围，从而为布林通道的建立提供准确的数据。
"""
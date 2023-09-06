import math
import numpy as np
import pandas as pd
#import statsmodels.api as sm
import matplotlib.pyplot as plt

gld = pd.read_csv('GLD.csv', index_col = 0, parse_dates = True)
gdx = pd.read_csv('GDX.csv', index_col = 0, parse_dates = True)

print(gld.info())
"""
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 385 entries, 2006-05-22 to 2007-11-29
Data columns (total 6 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   Open       385 non-null    float64
 1   High       385 non-null    float64
 2   Low        385 non-null    float64
 3   Close      385 non-null    float64
 4   Adj Close  385 non-null    float64
 5   Volume     385 non-null    int64  
dtypes: float64(5), int64(1)
memory usage: 21.1 KB
"""



OBS = 252
y = np.array(gld['Adj Close'][0:OBS])
x = np.array(gdx['Adj Close'][0:OBS])

# 增加一列常數項
X = np.column_stack((np.ones(len(x)), x))

plt.figure(figsize=(9, 5))
plt.subplot(211)
plt.plot(y, lw=1.5, label='gld')
plt.plot(y, 'ro')
plt.grid(True)
plt.legend(loc=0)
plt.ylabel('$Price$')
plt.title('Time Serice of Prices')

plt.subplot(212)
plt.plot(x, 'g', lw=1.5, label='gdx')
plt.plot(x, 'bx')
plt.grid(True)
plt.legend(loc=0)
plt.ylabel('$Price$')
plt.xlabel('$Date$')
plt.show()

# 跑回歸分析
model = sm.OLS(y, X)
results = model.fit()
hedgeRatio = results.params[1]
# 第一項是截距項 

import numpy as np

OBS = 252
y = np.array(gld['Adj Close'][0:OBS])
x = np.array(gdx['Adj Close'][0:OBS])

# 增加一列常數項
X = np.column_stack((np.ones(len(x)), x))

# 手動進行線性回歸
beta = np.linalg.lstsq(X, y, rcond=None)[0]

# 取得斜率（hedgeRatio）
hedgeRatio = beta[1]
hedgeRatio


gld_adjClose = gld['Adj Close']
gdx_adjClose = gdx['Adj Close']
spread = gld_adjClose - hedgeRatio * gdx_adjClose
#hedge ratio = 1.28 -> 4:5
spreadTrain = spread[0:OBS] # . 訓練集

plt.figure(figsize=(9, 5))
plt.plot(spread, lw=1.5, label='spread')
plt.plot(spreadTrain, 'ro', label='Train')
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('$Date$')
plt.ylabel('$Spread Price$')
plt.title('Pair Trade Performance')
plt.show()


#價差的平均數
spreadMean = spreadTrain.mean()
#價差的std
spreadStd = spreadTrain.std()
print(spreadMean)# 17.15193858784075
print(spreadStd) # 1.7234602680416338

#算價差的z-score
zscore = (spread - spreadMean) / spreadStd


#spread = gld_adjClose - hedgeRatio * gdx_adjClose
longs = zscore <= -2 # 跌到兩個標準差以下 買
# long gld , short gdx
shorts = zscore >= 2 # 升到超過兩個標準差 賣
# long gdx , short gld
# long short 以4:5的比例執行

exits = np.abs(zscore) <= 1 # 出場

positions = np.array(len(spread)*[None, None])
positions.shape = (len(spread), 2)


for i, b in enumerate(shorts):
    if b:
        positions[i] = [-1, 1]

for i, b in enumerate(longs):
    if b:
        positions[i] = [1, -1]

for i, b in enumerate(exits):
    if b:
        positions[i] = [0, 0]

# 沒有動作 -> 維持前一天動作
for i, b in enumerate(positions):
    if b[0] == None :
        positions[i] = positions[i-1]
    

print(positions[:10])
print(positions[-10:])
"""
[[-1 1]
 [-1 1]
 [-1 1]
 [-1 1]
 [-1 1]
 [-1 1]
 [0 0]
 [0 0]
 [0 0]
 [0 0]]
[[-1 1]
 [-1 1]
 [-1 1]
 [-1 1]
 [-1 1]
 [-1 1]
 [-1 1]
 [-1 1]
 [-1 1]
 [-1 1]]
"""

OBS = 385
cl1 = np.array(gld['Adj Close'][0:OBS])
cl2 = np.array(gdx['Adj Close'][0:OBS])

ret_cl1 = np.diff(cl1) / cl1[:-1] #算報酬率
ret_cl2 = np.diff(cl2) / cl2[:-1]

dailyret = np.concatenate((ret_cl1, ret_cl2), axis=0)
print(dailyret)

# 調整為度
dailyret = np.reshape(dailyret, (OBS-1, 2), order = 'F')
print(dailyret)

# 部位 ＊ return
PL = positions[:-1] * dailyret
pnl = np.sum(PL, axis = 1)

plt.figure(figsize=(9, 5))
plt.plot(pnl, lw=1.5, label='pnl')
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('$Date$')
plt.ylabel('$Profit_Loss$')
plt.title('Strategy PL')
plt.show()


total = np.sum(pnl)
print(total) # 0.2333645617327999

# sharp ratio
sharpTrainset = math.sqrt(252)*np.mean(pnl[0:251])/np.std(pnl[0:251]) # 前半段資料 訓練
sharpTestset = math.sqrt(252)*np.mean(pnl[252:OBS-1])/np.std(pnl[252:OBS-1]) # 測試集
print('sharpTrainset: ', sharpTrainset) # sharpTrainset:  1.9739039675788428
print('sharpTestset: ', sharpTestset) #sharpTestset:  1.087713913941673
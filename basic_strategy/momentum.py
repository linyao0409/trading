# 動能策略 -> 相信趨勢會持續
# 多頭 ：買
# 空頭 ：賣

# 盤整策略 均值回歸特性

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sp500 = pd.read_csv('GSPC_2000_2014.csv', index_col = 0, parse_dates = True)
print(sp500.info())
# 42日均線
sp500['42d'] = np.round(sp500['Close'].rolling(window=42, center=False).mean(), 2)
# 252日均線
sp500['252d'] = np.round(sp500['Close'].rolling(window=252, center=False).mean(), 2)

# close price
plt.figure(figsize=(9, 5))
plt.plot(sp500['Close'])
plt.grid(True)
plt.show()

# volume
plt.figure(figsize=(20,10))
plt.plot(sp500[["Volume"]])
plt.grid(True)


# close 42day 252day
plt.figure(figsize=(9, 5))
plt.plot(sp500[['Close', '42d', '252d']])
plt.grid(True)
plt.show()


#短期向上突破長期是一個訊號 市場往上移動
sp500['42-252'] = sp500['42d'] - sp500['252d']
print(sp500['42-252'].tail())
plt.plot(sp500["42-252"])
plt.grid(True)

# 短期與長期差距超過50點時候紀錄
SD = 50
sp500['Regime'] = np.where(sp500['42-252'] > SD, 1, 0)
sp500['Regime'] = np.where(sp500['42-252'] < -SD, -1, sp500['Regime'])
print(sp500['Regime'].value_counts())

"""
Regime
 1    1488
 0    1232
-1     871
Name: count, dtype: int64
"""

plt.figure(figsize=(9, 5))
plt.plot(sp500[['Regime']])
plt.ylim([-1.1, 1.1])
plt.grid(True)
plt.show()

# 用對數報酬計算績效
sp500['Market'] = np.log(sp500['Close']/sp500['Close'].shift(1))
sp500['Strategy'] = sp500['Regime'].shift(1) * sp500['Market']

# 用pandas 畫的
sp500[['Market', 'Strategy']].cumsum().apply(np.exp).plot(grid=True, figsize=(9, 5))
plt.show()
# 畫出市場績效 跟策略績效 (cumsum) (np.exp) 計算用對數報酬 故還原
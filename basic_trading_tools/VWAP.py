import numpy as np

c,v = np.loadtxt('data.csv',delimiter=",",usecols=(6,7),unpack=True)
# c: close
# v: volume
print(c)
print(type(c)) # <class 'numpy.ndarray'>
"""
[336.1  339.32 345.03 344.32 343.44 346.5  351.88 355.2  358.16 354.54
 356.85 359.18 359.9  363.13 358.3  350.56 338.61 342.62 342.88 348.16
 353.21 349.31 352.12 359.56 360.   355.36 355.76 352.47 346.67 351.99]
"""
print(v)
print(type(v)) # <class 'numpy.ndarray'>
"""
[21144800. 13473000. 15236800.  9242600. 14064100. 11494200. 17322100.
 13608500. 17240800. 33162400. 13127500. 11086200. 10149000. 17184100.
 18949000. 29144500. 31162200. 23994700. 17853500. 13572000. 14395400.
 16290300. 21521000. 17885200. 16188000. 19504300. 12718000. 16192700.
 18138800. 16824200.]
"""

# calculate VWAP (value weighter average price)
# 用交易量當作權重計算加權平均
vwap = np.average(c,weights=v)
print(vwap) # 350.5895493532009

# np 統計函數
np.max(c) # maximum
np.min(c) # minimum
# 中位數
np.median(c) #median
# 排序
sorted_close = np.msort(c)
print(sorted_close)
"""
[336.1  338.61 339.32 342.62 342.88 343.44 344.32 345.03 346.5  346.67
 348.16 349.31 350.56 351.88 351.99 352.12 352.47 353.21 354.54 355.2
 355.36 355.76 356.85 358.16 358.3  359.18 359.56 359.9  360.   363.13]
"""

# 變異數
np.var(c)
# standard error
(np.var(c))**(0.5)






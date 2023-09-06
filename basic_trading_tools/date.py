import numpy as np

from datetime import datetime


nddates,ndclose=(np.loadtxt('data.csv',dtype="str",delimiter=",",usecols=(1,6),unpack=True))

print(nddates)
"""
['28-01-2011' '31-01-2011' '01-02-2011' '02-02-2011' '03-02-2011'
 '04-02-2011' '07-02-2011' '08-02-2011' '09-02-2011' '10-02-2011'
 '11-02-2011' '14-02-2011' '15-02-2011' '16-02-2011' '17-02-2011'
 '18-02-2011' '22-02-2011' '23-02-2011' '24-02-2011' '25-02-2011'
 '28-02-2011' '01-03-2011' '02-03-2011' '03-03-2011' '04-03-2011'
 '07-03-2011' '08-03-2011' '09-03-2011' '10-03-2011' '11-03-2011']
"""
print(ndclose)
"""
['336.1' '339.32' '345.03' '344.32' '343.44' '346.5' '351.88' '355.2'
 '358.16' '354.54' '356.85' '359.18' '359.9' '363.13' '358.3' '350.56'
 '338.61' '342.62' '342.88' '348.16' '353.21' '349.31' '352.12' '359.56'
 '360' '355.36' '355.76' '352.47' '346.67' '351.99']
"""

print(type(nddates)) # <class 'numpy.ndarray'>
print(nddates.shape) # (30,)

def price2flt(ndarray):
    lst_price = list(ndarray)
    flt_price = list()
    num = len(lst_price)

    for i in range(num):
        flt_price.append(float(lst_price[i]))
    return flt_price

flt_price = price2flt(ndclose)
print(flt_price)
"""
[336.1, 339.32, 345.03, 344.32, 343.44, 346.5, 351.88, 355.2, 358.16, 354.54, 356.85, 359.18, 359.9, 363.13, 358.3, 350.56, 338.61, 342.62, 342.88, 348.16, 353.21, 349.31, 352.12, 359.56, 360.0, 355.36, 355.76, 352.47, 346.67, 351.99]
"""

#學習datetime.strptime!!
# datetime.strptime("04-09-1998","%d-%m-%Y") -> 
birth = (datetime.strptime("04-09-1998","%d-%m-%Y")) 
# 1998-09-04 00:00:00
print(birth.date()) # 1998-09-04
print(birth.date().weekday()) # 4 (thuresday)

# 把日期字串ndarray轉成星期幾的數值串列
def datestr2num(ndarray):
    list_date = list(ndarray)
    weekdates = list()
    num = len(list_date)

    for i in range(num):
        weekdates.append(datetime.strptime(ndarray[i],"%d-%m-%Y").date().weekday())
    return weekdates

weekdates = datestr2num(nddates)
print(weekdates)
"""[4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
"""

# weeksummary
nddates,ndopen,ndhigh,ndlow,ndclose = np.loadtxt('data.csv',dtype="str",delimiter=",",usecols=(1,3,4,5,6),unpack=True)

dates = datestr2num(nddates)
open = price2flt(ndopen)
high = price2flt(ndhigh)
low = price2flt(ndlow)
close = price2flt(ndclose)


close = close[:16]
dates = dates[:16]
print("___")
# get first Monday
dates = np.array(dates)
print(dates)
index = np.where(dates==0)
print(index) # (array([ 1,  6, 11]),)
x = (np.ravel(index))
print(x) # [ 1  6 11]
print(x[0]) # 1

first_monday = np.ravel(np.where(dates==0))[0]
print(first_monday) # 1

# np.ravel 的用法 平坦化ndarray
# np.ravel(ndarray,order=)
x = np.array([[1,2,3],[4,5,6]])
print(np.ravel(x)) # [1 2 3 4 5 6]

#last Friday
last_Friday = np.ravel(np.where(dates==4))[-1]
print(last_Friday) # 15






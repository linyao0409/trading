import numpy as np
import sys

N = 5
c = np.loadtxt('data.csv',delimiter=",",usecols=(6,),unpack=True)

b = c[-N:]
print(f"b:{b}")
rb = b[::-1]
print(f"rb{rb}")

#b:[355.36 355.76 352.47 346.67 351.99]
#rb[351.99 346.67 352.47 355.76 355.36]
A = np.zeros((N,N),float)
print(f"Zeros N by N \n{A}")
"""
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
"""

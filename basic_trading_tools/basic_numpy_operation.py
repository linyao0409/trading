import numpy as np
import timeit
# arange 
a1 = np.arange(5)
print(a1) # [0 1 2 3 4]
print(type(a1)) #<class 'numpy.ndarray'>

a2 = np.arange(2,5)
print(a2) # [2 3 4]
print(type(a2)) # <class 'numpy.ndarray'>

a1.shape = (5,1)
print(a1)

a3 = np.arange(2,12)
print(a3) # [ 2  3  4  5  6  7  8  9 10 11]
a3.shape = (5,2)
print(a3)
"""
[[ 2  3]
 [ 4  5]
 [ 6  7]
 [ 8  9]
 [10 11]]
 """

 # ndarray 多為的數組物件，資料都是同質的（整數 浮點數 ...)
print(a1.dtype)
a1.dtype = "float"
print(a1.dtype) # dtype 是 ndarray 的屬性

a4 = np.arange(5,13,dtype='f') # 創建屬性為浮點數的ndarray
print(a4)

#np.zeros方法
z1 = np.zeros(5,dtype=int)
z2 = np.zeros(5,dtype=float)
print(z1) # [0 0 0 0 0]
print(z2) # [0. 0. 0. 0. 0.]

#np.ones方法
o1 = np.ones(4,dtype=float)
print(o1) # [1. 1. 1. 1.]

# arange , linspace , random.random 方法
rng = np.arange(0,20,2) # 不含20
print(rng) # [ 0  2  4  6  8 10 12 14 16 18]

spc = np.linspace(0,1,5) # 5是切成幾份
print(spc) # [0.   0.25 0.5  0.75 1.  ]

rnd = np.random.random(4) # 4個 U[0,1]
print(rnd) #[0.60208102 0.68155741 0.69062269 0.58884776]

# ndarray numpy的陣列 
# 與list不同，ndarray的大小是固定的，
# 要改變大小只能刪除原先多維陣列，產生一個新的多為陣列
# 且ndarray所有元件大小皆相同 且類型相同 可用.dtype方法得知種類

# advantage:
# 更石和用於數學運算比較有效率且程式碼精簡

Mat = np.array([np.arange(2),np.arange(2)]) #[[0,1],[0,1]]
Mat.shape # (2,2) tuple
print(Mat)
print(Mat.shape)

# 生成ndarray的不同方法：

a = np.array([[1,2],[3,4]]) 
print(a[0,0]) # 1
print(a[0,1]) # 2 
print(a[1,0]) # 3
print(a[1,1]) # 4

# np.ones
o3 = np.ones((4,3),dtype = float)
print(o3)
"""
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
 """

# np.zeros
z3 = np.zeros((2,3),dtype=int)
print(z3)
"""
[[0 0 0]
 [0 0 0]]
"""

# np.full
f3 = np.full((3,4),2.71)
print(f3)
"""
[[2.71 2.71 2.71 2.71]
 [2.71 2.71 2.71 2.71]
 [2.71 2.71 2.71 2.71]]
"""

# np.random.random
r3 = np.random.random((2,3))
print(r3)
"""
[[0.55162649 0.09551931 0.76512702]
 [0.07977546 0.82165274 0.95549891]]
"""
# np.random.normal
n3 = np.random.normal(0,1,(4,3))
print(n3) # mu = 0 , std = 1?
"""
[[ 0.16183645  1.35572536 -0.26204873]
 [ 0.35477212  1.02252495 -1.57937111]
 [ 0.86478957 -1.2549873   0.53909438]
 [ 1.40652195 -0.38719854  1.06430194]]
"""

# np.random.randint
r3 = np.random.randint(5,10,(3,4))
print(r3) # 5 ~9 整數的亂數
"""
[[6 7 6 5]
 [8 7 8 9]
 [7 7 5 5]]
"""

# np.eye
e3 = np.eye(3)
print(e3)
"""
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""


# array's attribute

# ndarray.shape -> shape 
# ndarray.ndim -> dimension of array
# ndarray.itemsize -> 陣列中元素的大小
# ndarray.nbytes -> 整個陣列所有元素大小總計
# ndarray.T -> transpose of matrix （dim <=2 )
# 與self.transpose() 效果相同
# ndarray.flat ->把陣列扁平化輸出


Array1 = np.random.random((2,3))
print(Array1)
"""
[[0.90178495 0.22730438 0.7545462 ]
 [0.15709625 0.21107274 0.27263218]]
"""
print(Array1.shape) # (2, 3)
print(Array1.ndim) # 2
print(Array1.itemsize) # 8
print(Array1.nbytes) # 48 (6*8)
print(Array1.T)
print(Array1.flat)

# Mat = np.array()
#np.array(np.arange(2))
#print(np.arange(2))

Mat = np.array([np.arange(2),np.arange(2)],dtype=int)
print(Mat)
# [[0 1]
# [0 1]]

a = np.array([[1,2],[3,4]])
print(a)
"""
[[1 2]
 [3 4]]
 """

# 改變維度方法
# ndarray.flatten 
F = a.flatten()
print(F) # [1 2 3 4]
#print(F.item())
print(F[1]) # 2
print(F.item(1)) # 2

F.itemset(1,100)
print(F) # [  1 100   3   4]

# adjust dim using tuple
b = np.arange(12)
print(b.shape) # (12,) 
print(b)
"""[ 0  1  2  3  4  5  6  7  8  9 10 11]"""

b.shape = (3,4)
print(b.shape) # (3, 4)
print(b)
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

b = b.reshape(2,6)
print(b.shape) # (2, 6)
print(b)
"""
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
"""

print(b.transpose())
"""
 [ 1  7]
 [ 2  8]
 [ 3  9]
 [ 4 10]
 [ 5 11]]
"""
print(b)
"""
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
"""

a = np.arange(12).reshape(3,4)
print(a)
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

b = a*2
print(b)
"""
[[ 0  2  4  6]
 [ 8 10 12 14]
 [16 18 20 22]]
"""

#水瓶組合陣列
c = np.hstack((a,b))
print(c)
"""
[[ 0  1  2  3  0  2  4  6]
 [ 4  5  6  7  8 10 12 14]
 [ 8  9 10 11 16 18 20 22]]
"""
# 垂直
d = np.vstack((a,b))
print(d)


"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [ 0  2  4  6]
 [ 8 10 12 14]
 [16 18 20 22]]
"""
# 水平
e = np.concatenate((a,b),axis=1)
print(e)
"""
[[ 0  1  2  3  0  2  4  6]
 [ 4  5  6  7  8 10 12 14]
 [ 8  9 10 11 16 18 20 22]]
"""
# 垂直
f = np.concatenate((a,b,a),axis=0)
print(f)
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [ 0  2  4  6]
 [ 8 10 12 14]
 [16 18 20 22]
 [ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
 """
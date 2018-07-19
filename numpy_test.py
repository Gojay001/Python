#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# numpy_test.py

import numpy as np
# 属性
b = np.array([[1,2,4], [4,5,6]])
print(b)
print(b.ndim) # 维度
print(b.shape) # 行数和列数
print(b.dtype) # 指定数据类型
print(b.size) # 元素个数

# 创建
a = np.array([0, 2, 3, 4, 6])
print(a)
print(a[:3])
a1 = np.zeros(10) # 全0矩阵
print(a1)
a2 = np.zeros((3,4)) # 3行4列
print(a2)
a3 = np.ones((3,4,2)) # 3行4列2箱全1矩阵
print(a3)
a4 = np.empty((2,3)) # 2行3列空矩阵，元素都是接近0
print(a4)
a5 = np.ones_like(a4) # 产生和a4维度相同的全1矩阵
print(a5)
a6 = np.eye(5) # 创建5行5列单位矩阵
print(a6)
a7 = np.arange(3,15) # 类似于list的range()
print(a7)
a8 = a7.reshape((3,4)) # 改变数组形状:3行4列
print(a8)
a9 = np.linspace(1,10,20) #分割成20个数据，生成线段
print(a9)

# 运算
a = np.array([10,20,30,40]) # [10, 20, 30, 40]
b = np.arange(4) # [0, 1, 2, 3]
c = a - b  # [10 19 28 37]
print(c)
c1 = a * b # [  0  20  60 120]
print(c1)
c2 = b ** 2  # [0 1 4 9]
print(c2)
c3 = 10 * np.sin(a)
print(c3)
print(b < 3)
c_dot = np.dot(a,b) # 矩阵乘法运算
print(c_dot)
c_dot_2 = a.dot(b)
print(c_dot_2)
c4 = np.random.random((2,4)) # 2行4列[0-1]随机数
print(c4)
print(np.sum(c4))
print(np.min(c4))
print(np.max(c4))
print("sum =",np.sum(c4,axis=1)) # axis=1按行查找,0按列查找

# 索引
A = np.arange(3,15)
print(A[3])
A1 = np.arange(3,15).reshape((3,4))
print(A1[2])
print(A1[1, 1])
print(A1[1, 1:3])
for row in A1: # 按行输出
	print(row)
print(A1.flatten()) # 多维矩阵展开1列输出
for item in A1.flat: # flat迭代器
    print(item)

# 合并
A = np.array([1,1,1])
B = np.array([2,2,2])
C = np.vstack((A,B)) # vertical stack上下合并
print(C)
print(A.shape,C.shape)
D = np.hstack((A,B)) # horizontal stack左右合并
print(D)
print(A.shape,D.shape)
A1 = np.array([1,1,1])[:,np.newaxis] # 矩阵转置
print(A1)
B1 = B[:,np.newaxis]
print(B1)
C1 = np.concatenate((A1,B1,B1,A1),axis=0) #多个矩阵合并
print(C1)
D1 = np.concatenate((A1,B1,B1,A1),axis=1)
print(D1)

# 分割
A = np.arange(12).reshape((3, 4)) # 建立3行4列数组
print(A)
print(np.split(A, 2, axis=1)) # 纵向分割
print(np.split(A, 3, axis=0)) # 横向分割
print(np.array_split(A, 3, axis=1)) # 不等量分割
print(np.vsplit(A, 3)) #等于 print(np.split(A, 3, axis=0))
print(np.hsplit(A, 2)) #等于 print(np.split(A, 2, axis=1))

# copy
a = np.arange(4)
b = a
c = a.copy()
a[0] = 11
print(b is a, c is a)

# 更多用法
d = np.random.randn(20)
print((d > 0).sum()) # 数组统计方法
d.sort() # 排序
print(d)
name = np.array(['a', 'a', 'b', 'c', 'c'])
print(np.unique(name)) # 数组元素唯一化
## 存储、读取数组
d1 = np.random.rand(10, 5)
np.savetxt('file/np_array.txt', d1, delimiter='')
d2 = np.loadtxt('file/np_array.txt', dtype=bytes).astype(str)
np.save('file/array', d1)
d3 = np.load('file/array.npy')
#print(d2)
#print(d3)

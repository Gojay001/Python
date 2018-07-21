#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pandas_test.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series:索引在左边，值在右边
## Series基础
obj = pd.Series([2,4,5,np.nan,8])
print(obj)
print(obj.index) # 获取索引
print(obj.values) # 获取值
obj2 = pd.Series([2,3,8], index=['a','b','c']) # 自定义index
print(obj2)
print(obj2.index, obj2.values)
## Series运算
print(obj2 > 4)
print(obj2[obj2>4])
print(obj2 * 4)
s1 = pd.Series([1,2,3], index=['a','b','c'])
s2 = pd.Series([3,2,1], index=['c','b','a'])
print(s1 + s2)


# DataFrame :由Series组成的大字典,既有行索引也有列索引
## DataFrame基础
dates = pd.date_range('20180101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['a','b','c','d'])
print(df)
print(df['b']) # 根据索引来挑选数据('b')
df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1) # 不给定行、列索引，默认从0开始index
df2 = pd.DataFrame({'A' : 1.,
					'B' : pd.Timestamp('20180720'),
					'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
					'D' : np.array([3] * 4, dtype='int32'),
					'E' : pd.Categorical(['test','train','test','train']),
					'F' : 'foo'})
print(df2) # 对每一列数据进行特殊处理
print(df2.dtypes) # 查看数据类型
print(df2.index) # 列
print(df2.columns) # 行
print(df2.values) # 值
print(df2.describe()) # 数据总结
print(df2.T) # 转置
print(df2.sort_index(axis=1, ascending=False)) # index排序
print(df2.sort_values(by='B')) # values排序

## 筛选数据
df3 = pd.DataFrame(np.arange(24).reshape(6,4), index=dates, columns=['A','B','C','D'])
### 简单按行、列筛选数据
print(df3.A) # 按列筛选
print(df3['B'])
print(df3[0:3]) # 按行筛选
print(df3['20180101':'20180104'])
### 根据标签筛选数据:loc
print(df3.loc['20180103']) 
print(df3.loc[:,['A','B']])
print(df3.loc['20180101', ['A','B']])
### 根据序列筛选数据:iloc
print(df3.iloc[3,1])
print(df3.iloc[3:5, 1:3])
print(df3.iloc[[1,3,5], 1:3])
### 混合筛选数据:ix(弃用)
#print(df3.ix[:3,['A','C']])
### 根据判断筛选数据
print(df3[df3.A>8])

## 设置值
### 根据位置设置:loc、iloc
df3.iloc[2,2] = 1111
df3.loc['20180101','B'] = 2222
print(df3)
### 根据条件设置
df3.B[df3.A>4] = 0
print(df3)
### 按行或列设置
df3['F'] = np.nan
print(df3)
### 添加Series序列(长度必须对齐)
df3['E'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20180101',periods=6))
print(df3)

## 处理丢失数据
### 直接去掉有 NaN 的行或列:pd.dropna()
df3.iloc[0,0] = np.nan
print(df3.dropna(
	axis=1, # 0: 对行进行操作; 1: 对列进行操作
	how='any' # 'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop
	))
### 将 NaN 的值用其他值代替:pd.fillna()
print(df3.fillna(value=0))
### 判断是否有缺失数据 NaN, 为 True 表示缺失数据
print(df3.isnull())
### 检测在数据中是否存在 NaN, 如果存在就返回 True
print(np.any(df3.isnull()) == True)


# pandas文件的导入导出
sale = pd.read_excel('/Users/gojay/Downloads/sale.xls', header=0, index_col=u'日期', nrows=200)
print(sale)
#data.to_excel('temp.xlsx') # 写入文件
stat = sale.describe() # 数据分析
print(stat)
print(stat.loc['max'] - stat.loc['min']) # 极值
plt.figure()
sale.boxplot()
plt.show()


# pandas可视化
## Series
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
datasum = data.cumsum() # 累加
datasum.plot()
plt.show()
## Dataframe
### plot画图: 线性图
data = pd.DataFrame(
	np.random.randn(1000,4),
	index=np.arange(1000),
	columns=list('ABCD')
	)
datasum = data.cumsum()
datasum.plot() 
plt.show()
### scatter画图: 散点图
ax = datasum.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
datasum.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()


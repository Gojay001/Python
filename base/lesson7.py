#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('/Users/gojay/Downloads/data721.xls', index_col=0, header=None)
#print(data.describe())
data.index.name = 'date'
data.columns = ['sale1', 'sale2', 'sale3']
# 缺省值处理
# print(data.isnull())
data['sale1'] = data['sale1'].fillna(data['sale1'].mean())
data['sale2'] = data['sale2'].fillna(data['sale2'].median())
data = data.dropna()
print(data.isnull().sum())
# print(data.interpolate(method='cubic')) # 插值
print(data.head(3))
print(data.tail(3))
# 离散化
d = pd.cut(data['sale3'], bins=range(0,5000,500), right=False, labels=list('ABCDEFGHI'))
data['sale3'] = d.values
data1 = data[data['sale3']=='A']
# print(data1)
# data.hist()
# data.plot()
# plt.show()

# 数据规范化
## 最大最小规范化
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
# data[['sale1', 'sale2']] = scaler.fit_transform(data[['sale1', 'sale2']])
# print(data)
## 标准化(z-score)
from sklearn.preprocessing import StandardScaler
scaler1 = StandardScaler()
data[['sale1', 'sale2']] = scaler1.fit_transform(data[['sale1', 'sale2']])
print(data)
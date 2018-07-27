#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# count_data.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取文件所有数据
data = pd.read_excel('/Users/gojay/Downloads/data2.xls', header=None)
data.columns = ['date', 'number']
#data = data.set_index(1)
datacount = data.number.count()

# 获取指定区间的统计数据
def getdata(low, high):
	group1 = data[data>low]
	group2 = group1[group1<high]
	group2 = group2.dropna(axis=0, how='any') # 去掉NaN

	count = group2.number.count() # 频数
	countarray.append(count)
	frequency = count / datacount # 频率
	frearray.append(frequency)
	global countfre
	countfre += frequency # 累计频率
	countfrearray.append(countfre)
	mean = group2.number.mean() # 平均值
	meanarray.append(mean)
	median = group2.median().loc['number'] # 中位数
	medianarray.append(median)
	
# 统计数据数组
countfre = 0.0 # 累计频率
countarray = [] # 频数
frearray = [] # 频率
countfrearray = [] # 累计频率
meanarray = [] # 平均值
medianarray = [] # 中位数
dataindex = [] # 索引

# 步长为500循环统计数据
i = 0
while(i <= data.number.max()):
	low = i
	high = i+500
	temp = '[%d-%d)' % (low,high) # 索引格式
	dataindex.append(temp)
	getdata(low, high) # 获取统计数据
	i += 500

# 统计数据数组转为Series
datacount = pd.Series(countarray, index=dataindex)
datafre = pd.Series(frearray, index=dataindex)
datacountfre = pd.Series(countfrearray, index=dataindex)
datamean = pd.Series(meanarray, index=dataindex)
datamedian = pd.Series(medianarray, index=dataindex)

# 建立DataFrame展示数据
data = pd.DataFrame({'频数' : datacount,
					'频率' : datafre,
					'累计频率' : datacountfre,
					'平均值' : datamean,
					'中位数' : datamedian})
print(data)

# 写入文件
data.to_excel('temp.xlsx')

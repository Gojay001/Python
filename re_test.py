#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# re_test.py

__author__ = 'gojay'

import re
import json

reg_start = re.compile('{') # json开始
reg_end = re.compile('}') # json结束
reg_jump = re.compile('_heartbeat_') # 跳过该json

# 信息类
class Information(object):
	def __init__(self, a, c, tz, hh, r, u):
		self.a = a
		self.c = c
		self.tz = tz
		self.hh = hh
		self.r = r
		self.u = u

	# 返回该对象属性信息
	def tostring(self):
		return self.a, self.c, self.tz, self.hh, self.r, self.u

	# a:浏览器
	def get_a(self):
		return self.a

	# c:国家
	def get_c(self):
		return self.c

	# tz:地区
	def get_tz(self):
		return self.tz

	# hh:路径
	def get_hh(self):
		return self.hh

	# r:URL地址
	def get_r(self):
		return self.r

	# u:资源
	def get_u(self):
		return self.u

# 存储信息列表
infolist = []

# 读取文件
def readtext(path):
	count = 0 
	with open(path, 'r') as f:
		for line in f.readlines():
			# 获取count个json
			if count > 10:
				break
			if reg_jump.findall(line):
				continue
			if reg_end.findall(line):
				#print(line)
				info = json.loads(line, object_hook=jsontoinfo)
				infolist.append(info)
				count += 1

# json转为类对象
def jsontoinfo(info):
	return Information(info['a'], info['c'], info['tz'], info['hh'], info['r'], info['u'])

# 读取文件，获取关键key-value
if __name__ == '__main__':
	
	# 输入需要读取文件的路径
	path = '/Users/gojay/Downloads/file1.txt'
	text = readtext(path)

	# 输出所有信息的关键key-value
	pos = 1
	for info in infolist:
		print("第%d条信息：" % pos)
		print('浏览器:', info.get_a())
		print('国家:', info.get_c())
		print('地区:', info.get_tz())
		print('路径:', info.get_hh())
		print('URL地址:', info.get_r())
		print('资源:', info.get_u())
		print()
		pos += 1


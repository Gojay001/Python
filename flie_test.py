#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file_test.py

import os
import shutil

# 创建目录及文件
def createdir(sourcedir):
	if os.path.isdir(sourcedir):
		shutil.rmtree(sourcedir)
	os.mkdir(sourcedir)
	for x in range(5):
		with open(os.path.join(sourcedir, '%d.txt' % (x+1)), 'w') as f:
			f.write('这是第 %d 个文件!' % (x+1))

# 移动文件
def movefile(sourcedir, destdir):
	if os.path.isdir(destdir):
		shutil.rmtree(destdir)
	os.mkdir(destdir)
	for x in os.listdir(sourcedir):
		print(x)
		if os.path.isfile(os.path.join(sourcedir, x)):
			shutil.copyfile(os.path.join(sourcedir, x), os.path.join(destdir, x))
			print('成功移动:', x)

sourcedir = '/Users/gojay/test'
destdir = '/Users/gojay/test1'
createdir(sourcedir)
#movefile(sourcedir, destdir)
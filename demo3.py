#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 遍历技巧
# 字典遍历时，使用items()方法获取K-V
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)

# 序列遍历时，使用enumerate()函数获取索引位置和对应值
for i, v in enumerate(['tic', 'tac', 'toc']):
	print(i, v)

# 同时遍历两个或更多的序列，可以使用zip()组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print(q, a)

# 排序:sorted();反向遍历:reversed()
for x in sorted(range(1, 10, 2)):
	print(x, end = ' ')
for i in reversed(range(1, 10, 2)):
	print(i, end = ' ')
print()

import sys
print(sys.path)

# os模块
import os
print(os.name)
print('操作系统信息:', os.uname())
print('环境变量:', os.environ)
print('PATH路径:', os.environ.get('PATH'))
print('当前目录的绝对路径:', os.path.abspath('.'))
os.mkdir('/Users/gojay/testdir') # 新建目录
os.rmdir('/Users/gojay/testdir') # 删除目录
print('合并路径:', os.path.join('/Users/gojay', 'file'))
print('分割路径:', os.path.split('/Users/gojay/file.txt'))
print('得到文件扩展名:', os.path.splitext('/Users/gojay/file.txt'))
#os.rename('temp.txt', 'test.txt') # 文件重命名
#os.remove('test.txt') # 删除文件
# 列出当前目录下所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出当前目录下所有.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# shutil模块:os模块补充
import shutil
#shutil.copyfile('temp.txt', 'text.txt') # 复制文件

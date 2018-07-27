#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 调用oop_test.py模块
import sys
sys.path.append('/Users/gojay/Python')
import oop_test
oop_test.ComputerScienceCollege.IS(120).exam()
# import turtle_test

# 调用matplotlib画图
def plotcos():
	import matplotlib.pyplot as plt
	import numpy as np
	x = np.linspace(0, 2 * np.pi, 50)
	y = np.cos(x)
	plt.plot(x, y)
	plt.show()
#plotcos()

# 调用matplotlib做动画
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/10.0))
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line,
ani = animation.FuncAnimation(fig=fig,
                              func=animate,
                              frames=100,
                              init_func=init,
                              interval=20,
                              blit=False)
#plt.show()

# 正则表达式
# \d可以匹配一个数字
# \w可以匹配一个字母或数字或下划线
# \s可以匹配一个空格（也包括Tab等空白符）
# .可以匹配任意字符
# *表示任意个字符（包括0个）
# +表示至少一个字符
# ?表示0个或1个字符
# {n}表示n个字符
# {n,m}表示n-m个字符
# 要做更精确地匹配，可以用[]表示范围:
# [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线
# [0-9a-zA-Z\_]+可以匹配至少由一个...组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符
# A|B可以匹配A或B
# ^表示行的开头:^\d表示必须以数字开头
# $表示行的结束:\d$表示必须以数字结束

# re模块
import re
# 匹配字符串:match()
# 如果匹配成功，返回一个Match对象，否则返回None
p = re.compile('[abc]') # 编译
print(p)
print(p.match('afdf')) # 使用(不需要正则字符串)
print(p.match('caccb'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
# 切分字符串:split()
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
# 分组:用()表示group
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0), m.group(1), m.group(2))
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
# 加上?转为非贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
# 验证是否合法邮箱
def is_valid_email(addr):
    re_email = re.compile(r'^([1-9a-zA-Z]\w+)(\.\w+)+?(@\w+\.[a-zA-Z]+)$')
    return re_email.match(addr)
print(is_valid_email('gao.jay.test@126test.cn'))

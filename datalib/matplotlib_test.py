#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# matplotlib_test.py

import matplotlib.pyplot as plt
import numpy as np

# 基本用法
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
#plt.figure() # 定义一个图像窗口
plt.figure(num=3, figsize=(8, 5)) # 编号为3；大小为(8, 5)
l1, = plt.plot(x, y2, label='linear line') # 画(x ,y)曲线
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='square line')
#plt.legend(loc='upper right') # 显示label图例
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')
#plt.xlim((-1, 2)) # 设置x坐标轴范围
#plt.ylim((-2,3)) # 设置y坐标轴范围
#plt.xlabel('I am x') # 设置x坐标轴名称
#plt.ylabel('I am y')# 设置y坐标轴名称
new_ticks = np.linspace(-2, 2, 5) 
plt.xticks(new_ticks) # 设置x轴刻度
plt.yticks([-2, -1, 3],[r'$bad$', r'normal', r'good'])
ax = plt.gca() # 获取当前坐标轴信息
ax.spines['right'].set_color('none') # 右边框颜色设为默认
ax.spines['top'].set_color('none') # 上边框颜色设为默认
ax.xaxis.set_ticks_position('bottom') # 设置x坐标刻度的位置
ax.spines['bottom'].set_position(('data', 0)) # 设置边框位置
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
## 标注出点(x0,y0)的位置信息,画出一条垂直于x轴的虚线
x0 = 1
y0 = 2*x0 + 1
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)
plt.scatter([x0, ], [y0, ], s=50, color='b') # set dot styles
## 添加注释 annotate
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
## 添加注释 text
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})
## tick 能见度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    # 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))
plt.show() # 显示图像

'''
# 画3D图
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
t = np.linspace(0, 2*np.pi, 100)
xs, ys = np.meshgrid(t, t)
z = xs**2 - ys**2
ax.plot_surface(xs,ys,z)
plt.show()
'''
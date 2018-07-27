#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 运算符
print(3 ** 8)
print(3 / 8)
print(3 // 8)
print(int('0100'))
print(int('0100', 8))
print(int('0x40', 16))
a = 676
b = 324
c = 12
print(a > b, a < b, a == b, a != b, a < b and a < c)
# 四舍五入
a1 = 3.14
a2 = 3.66
print(round(a1), round(a2))

import math
# 向下取整
print(math.floor(3.66))
# 向上取整
print(math.ceil(3.14))
# 舍去小数取整
print(int(3.66))
# 指定精度
import decimal
a = decimal.Decimal(59)
b = decimal.Decimal('23.345')
print(a + b)
# python复数
a = -.32 + 4j
print(a, a.real, a.imag)

# 字符编码
print ord('a')
print chr(105)
# 字符串比较
print 'a' == 'b'
print 'ab' < 'ac'
print '' < 'b'

# 字符串常用方法
# find:字符串查找，找到返回下标，未找到返回-1;
# 格式:s.find(sub[,start][,end])
s = 'apple,peach,banana,peach,pear'
print(s.find('peach'), s.find('peach', 8), s.find('test'))
# split:字符串分离，返回字符串分离后子串;
# 格式:不带参数按空格分离
s1 = 'apple+peach+banana+pear'
s2 = s1.split('+')
print(s2)
# join:字符串连接
s3 = '-'.join(s2)
print(s3)
# 字符串大小写
s4 = 'ABCDefgHI'.lower()
s5 = s4.upper()
print(s4, s5)
# 字符串格式化:%d,%s,%f
price = 100
print("this is %d yuan" % price)
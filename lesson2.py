#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 判断年份是否闰年
def isYear(year):
	if year % 4 == 0 and year % 100 != 0:
		print("%d年是闰年" % year)
	elif year % 400 == 0:
		print("%d年是闰年" % year)
	else:
		print("%d年不是闰年" % year)
	return
#year = int(input("输入年份:"))
#isYear(year)

# 计算1-100奇数和
def addOdds(num):
	sum = 0
	for x in range(num):
		if x % 2 != 0:
			sum += x
	print(sum)
	return
#addOdds(100)

# 计算1-100之和
def addNum(num):
	sum = 0
	for x in range(num):
		sum += x
	print(sum)
	return
#addNum(101)

# 判断是否质数
def isPrime(num):
	if num < 1:
		print("输入格式有误")
		return
	if num == 1:
		print("1是质数")
		return
	flag = 1
	for x in range(2, num):
		if num % x == 0:
			print("%d不是质数" % num)
			flag = 0
			break;
	if flag != 0:
		print("%d是质数" % num)
	return
#isPrime(199)
'''
num = int(input("enter number:"))
while num != 0:
	isPrime(num)
	num = int(input("enter number:"))
'''

# 统计不为3的个数
L1 = [1,3,4,3,4,4,6,8,3,2,1,6]
count = 0
for num in L1:
	if num == 3:
		continue
	count += 1
print("3的个数:", count)

# 计算球体体积
def culVolume(radius, PI = 3.14):
	return 3.0/4 * PI * pow(radius, 3)
print("体积为:", culVolume(4))

# 计算n的阶乘
def factorial(n):
	if n < 1:
		print("输入格式错误")
		return
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)
print("阶乘为:", factorial(5))

# Fibonacci series: 斐波纳契数列
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b #使用 yield
        # print b 
        a, b = b, a + b 
        n = n + 1
for x in fab(6): 
    print(x, end = ' ')

# 全部字符大写
print()
L = ['abc', 'AbC', 'eFG']
print("列表转大写:", [x.upper() for x in L])
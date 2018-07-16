#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 输入输出
#age = input('enter your age:')
#print('age is:', age)
#print('Hi, id:%s, your age is:%d' % (str(2), int(age)))

#print('%2d-%02d' % (3, 1))
#print('%.2f' % 3.1415926)
#print('Hi, {0}, 收益为 {1:.1f}%'.format('gojay', 17.125))
#print(r'test\nte\'\'st')
#print('''line1
#line2
#line3''')
#print('9/3=',9/3)
#print('10//3=', 10//3)


"""
# 条件判断
age = input("enter age:")
if int(age) >= 18:
	print('adult:', age)
elif int(age) >=12:
	print('teenager:', age)
else:
	print('child:', age)

# 循环
# for...in
sum = 0
# for x in [1 , 2, 3]:
# 	sum += x
for x in range(101):
	sum += x
print(sum)

#while
sum = 0
n = 99
while n > 0:
	sum += n
	n = n - 2
print(sum)
"""


"""
# list: 有序
books = ['JAVA', 'PYTHON', 'PHP']
books.append('JS')
books.insert(1, 'AI')
books.pop() #删除末尾元素
books.pop(1) #删除第i元素
print(books)
print(len(books))
print(books[-1]) #倒数i元素
L = ['Apple', 123, True]
s = ['python', 'java', ['html', 'css'], L]
print(s)

# tuple: 不可变
t = (1, 2) 
t0 = ()
t1 = (1,)
t3 = ('a', 'b', ['A', 'B'])
t3[2][0] = 'X'
t3[2][1] = 'Y'
print(t3)
"""

# dictionary: 索引
books = {'java': 100, 'python': 90, 'php': 80}
books['asp'] = 70
print(books)
print(books['python'])
print('python' in books) #key是否存在
print(books.get('js', -1)) #key不存在返回-1
print(books.get('asp', -1))
books.pop('asp')


# dictionary(key-value)
d = {'java': 100, 'python': 150, 'js': 120}
# 检查key是否存在
if 'java' in d:
	print(d['java'])
print(d.get('test', -1))
# 增加、删除
d['php'] = 130
d.pop('js')
print(d)
#key只能是不可变对象
key = [1, 2, 3]
# d[key] = 'a list'

# set(不能重复)
s = set([1, 2, 3, 1, 3])
print s
s1 = set([1, 2, 3])
s1.add(4)
s1.remove(2)
print(s1, s1 & s, s1 | s)
s2 = ['a', 'c', 'b']
s2.sort()
s2.pop(2)
del s2[1]
print(s2)

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b)
    a, b = b, a + b
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# OOP
# 封装
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
    	return self.__name

    def get_score(self):
    	return self.__score

    def set_name(self, name):
    	self.__name = name

    def set_score(self, score):
    	self.__score = score

one = Student("tom", 7)
one.set_score(8)
print(one.get_name(), one.get_score())
print(one._Student__name) # python解释器自动更改内部变量名


# 继承、多态
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def just_run(animal):
	animal.run()

just_run(Dog())

# 检测类型
a = list()
b = Animal() 
c = Dog()
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(b, Dog))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
print(type(c))

# IO
with open('temp.txt', 'w') as f:
    f.write('Hello, world!\ntest')

with open('temp.txt', 'r') as f:
	for line in f.readlines():
		print(line.strip())
    #print(f.read())

# StringIO、BytesIO
from io import StringIO
f = StringIO()
f.write('hello')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

# 异常(n/0)
# try-except-finally
import logging
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    finally:
        print('finally...')
main()

# raise
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
bar()

# 自定义异常
class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
foo('0')

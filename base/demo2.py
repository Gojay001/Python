#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 传不可变对象实例
def changeInt(a):
    a = 10 
b = 2
changeInt(b)
print("b") #结果是2


# 传可变对象实例
def changeme(mylist):
    mylist.append([1,2,3,4])
    print("inner:", mylist)
    return
mylist = [10,20,30]
changeme(mylist)
print("outer:", mylist)

# 关键字参数:顺序可以不一致
def printinfo(name, age):
    print("name: ", name)
    print("age: ", age)
    return
printinfo(age=20, name="lihua")

# 不定长参数:
# 加 * 的参数会以元组的形式导入
def printinfo1(arg1, *vartuple):
    print("输出:")   
    print(arg1)
    for var in vartuple:
        print(var)
    return
printinfo1(10)
printinfo1(70, 60, 50)
# 加 ** 的参数会以字典的形式导入
def printinfo2(arg1, **vardict):
    print ("输出: ")
    print (arg1)
    print (vardict)
    return
printinfo2(1, a=2, b=3)

# 使用 lambda 来创建匿名函数
sum = lambda arg1, arg2: arg1 + arg2
print("sum is:", sum(10, 20))

# 列表推导式
vec = [2, 4, 6]
print([3*x for x in vec])
print([[x, x**2] for x in vec])
print([3*x for x in vec if x > 3])
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])
print([str(round(355/113, i)) for i in range(1, 6)])

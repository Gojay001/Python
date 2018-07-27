#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 调试
# print(),assert,logging,pdb
import logging
logging.basicConfig(level=logging.INFO)
s = '1' # 0
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# 序列化:json
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 20, 88)

## 类对象转json: json.dumps(s)
# class的实例都有一个__dict__属性，它就是一个dict:
print(json.dumps(s, default=lambda obj: obj.__dict__))
'''
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))
'''

## json转类对象: json.loads(d)
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
person = json.loads(json_str, object_hook=dict2student)
print(person)
print(person.age)

# 常用内建模块
## datetime
### 获取当前日期和时间
from datetime import datetime
now = datetime.now() # 获取当前datetime
print(now)
print(type(now))
### 获取指定日期和时间
dt = datetime(2015, 9, 19, 12, 20)
print(dt)
### datetime转换为timestamp
print(dt.timestamp())
### timestamp转换为datetime
t = 1442636400.0
print(datetime.fromtimestamp(t)) # 本地时间(UTC+8:00时区)
print(datetime.utcfromtimestamp(t)) # UTC时间(UTC+0:00)
### str转换为datetime
cday = datetime.strptime('2015-06-01 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
### datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))
### datetime加减
from datetime import datetime, timedelta
print(now + timedelta(days=2, hours=12))



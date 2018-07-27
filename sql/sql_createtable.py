#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sql_createtable.py

import csv
import codecs
import pymysql

csv_filename = 'file/jd_0.csv'
table_name = 'test'

file = codecs.open(csv_filename, 'r', 'gbk')
reader = file.readline()
b = reader.split(',')
colum = ''
for a in b:
    if a == '':
        continue
    colum = colum + a + ' varchar(255),'
colum = colum[:-1]
# print(colum)

create = 'create table if not exists ' + table_name + \
    ' ' + '(' + colum + ')' + ' DEFAULT CHARSET=utf8'
data = 'LOAD DATA LOCAL INFILE \'' + csv_filename + '\' INTO TABLE ' + table_name + \
    ' character set utf8 FIELDS TERMINATED BY \',\' ENCLOSED BY \'\"\' LINES TERMINATED BY \'' + \
    r'\r\n' + '\' IGNORE 1 LINES;'
# print(create)

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='tour')

cursor = conn.cursor()
cursor.execute('SET NAMES utf8;')
cursor.execute('SET character_set_connection=utf8;')
cursor.execute(create)
cursor.rowcount

conn.commit()
cursor.close()
print('OK')

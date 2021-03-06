#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sql_insertdata.py

import pymysql
import csv
import codecs

# 获取mysql连接


def get_conn():
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='root', db='tour', charset='utf8')
    return conn

# 写入sql


def insert(cur, sql, args):
    cur.execute(sql, args)

# 读取csv文件


def read_csv_to_mysql(filename):
    with codecs.open(filename=filename, mode='r', encoding='gbk') as f:
        reader = csv.reader(f)
        head = next(reader)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into jd_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            for item in reader:
                if item[1] is None or item[1] == '':  # item[1]作为唯一键，不能为null
                    continue
                args = tuple(item)
                args = args[1:]
                # print(args)
                insert(cur, sql=sql, args=args)

            conn.commit()
        except Exception as e:
            conn.rollback()
            print('error', e)
        finally:
            cur.close()
            conn.close()
            print('ok')


if __name__ == '__main__':
    local_dir = 'file/jd_100.csv'
    read_csv_to_mysql(local_dir)

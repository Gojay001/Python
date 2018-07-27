#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sql_live.py

import pymysql
import csv
import codecs

# 获取mysql连接


def get_conn():
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='root', db='journey', charset='utf8')
    return conn

# 写入sql


def insert(cur, sql, args):
    cur.execute(sql, args)

# 读取csv文件


def read_csv_to_mysql(filename):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            for item in reader:
                if item[0] is None or item[0] == '':  # item[i]作为唯一键，不能为null
                    continue
                args = tuple(item)
                # args = args[1:]
                print(args)
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
    local_dir = 'file/info.csv'
    read_csv_to_mysql(local_dir)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sql_roadfare.py

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
        print(head)
        sql = 'insert into roadfare(start_id,start_name,aim_id,aim_name,cost) values(%s,%s,%s,%s,%s)'
        try:
            start = 1
            for item in reader:
                if item[0] is None or item[0] == '':  # item[i]作为唯一键，不能为null
                    continue
                args = tuple(item)
                # args = args[1:]
                # print(args[0])

                aim = 1
                while aim < 13:
                    fare = [start, args[0], aim, head[aim], item[aim]]
                    print(fare)
                    insert(cur, sql=sql, args=fare)
                    aim += 1
                start += 1

            conn.commit()
        except Exception as e:
            conn.rollback()
            print('error', e)
        finally:
            cur.close()
            conn.close()
            print('ok')


if __name__ == '__main__':
    local_dir = 'file/roadfare.csv'
    read_csv_to_mysql(local_dir)

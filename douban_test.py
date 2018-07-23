#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# douban_test.py

# 加载库
from urllib import request
from urllib.parse import urlencode, quote
import json
from bs4 import BeautifulSoup
import time

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Host': 'movie.douban.com'
}
# 获取所有标签
tags = []
url = 'https://movie.douban.com/j/search_tags?type=movie'
req = request.Request(url, headers=header)
response = request.urlopen(req, timeout=20)
result = response.read().decode('utf-8')
# 加载json为字典
result = json.loads(result)
tags = result['tags']
print(tags)
tags = tags[0:3]

# 定义一个列表存储电影的基本信息
movies = []
# 处理每个tag
for tag in tags:
    start = 0
    print(type(tag))
    # 不断请求，直到返回结果为空
    while True:
        # 拼接需要请求的链接，包括标签和开始编号
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + \
            quote(tag) + '&sort=recommend&page_limit=20&page_start=' + str(start)
        print(url)
        req = request.Request(url, headers=header)
        response = request.urlopen(req, timeout=20)
        result = response.read().decode('utf-8')
        result = json.loads(result)

        # 先在浏览器中访问一下API，观察返回json的结构
        # 然后在Python中取出需要的值
        result = result['subjects']

        # 返回结果为空，说明已经没有数据了
        # 完成一个标签的处理，退出循环
        if len(result) == 0:
            break

        # 将每一条数据都加入movies
        for item in result:
            movies.append(item)

        # 使用循环记得修改条件
        # 这里需要修改start
        start += 20

# 看看一共获取了多少电影
print(len(movies))


# 请求每部电影的详情页面
for x in range(0, len(movies)):
    url = movies[x]['url']
    req = request.Request(url, headers=header)
    response = request.urlopen(req, timeout=20)
    result = response.read().decode('utf-8')

    # 使用BeautifulSoup解析html
    html = BeautifulSoup(result, 'lxml')
    # 提取电影简介
    # 捕捉异常，有的电影详情页中并没有简介
    try:
        description = html.find_all("span", attrs={"property": "v:summary"})[
            0].get_text()
    except Exception as e:
        # 没有提取到简介，则简介为空
        movies[x]['description'] = ''
    else:
        # 将新获取的字段填入movies
        movies[x]['description'] = description
    finally:
        print(len(movies))

    # 适当休息，避免请求频发被禁止，报403 Forbidden错误
    time.sleep(0.5)

fw = open('file/douban_movies.txt', 'w')
# 写入一行表头，用于说明每个字段的意义
fw.write('title^rate^url^cover^id^description\n')
for item in movies:
    # 用^作为分隔符
    # 主要是为了避免中文里可能包含逗号发生冲突
    fw.write(item['title'] + '^' + item['rate'] + '^' + item['url'] + '^' +
             item['cover'] + '^' + item['id'] + '^' + item['description'] + '\n')
fw.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# urllib_test.py

# Get
from urllib import request
## urllib的request模块发送get请求:
def printinfo(url):
	with request.urlopen(url) as f:
		print('Status:', f.status, f.reason)
		for k, v in f.getheaders():
			print('%s: %s' % (k, v))
		data = f.read()
		print('Data:', data.decode('utf-8'))
#printinfo('https://api.douban.com/v2/book/2129650')

## 使用Request对象把请求伪装成浏览器:
def imitate(url):
	req = request.Request(url)
	req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
	with request.urlopen(req) as f:
		data = f.read()
		print('Status:', f.status, f.reason)
		for k, v in f.getheaders():
			print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))
#imitate('http://www.douban.com/')

## 发送get请求
def getinfo(url):
	from urllib.request import urlopen
	html = urlopen(url).read().decode('utf-8')
	return html

html = getinfo('https://morvanzhou.github.io/static/scraping/basic-structure.html')
# print(html)

## 使用正则表达式匹配信息
import re
### 获取<title>
res1 = re.findall(r'<title>(.+?)</title>', html)
### 获取<p>: flags=re.DOTALL 来对 tab, new line 不敏感
res2 = re.findall(r'<p>(.*?)</p>', html, flags=re.DOTALL)
### 获取所有链接
res3 = re.findall(r'href="(.*?)"', html)
print('\nPage title is: ', res1[0])
print('\nPage paragraph is:	 ', res2[0])
print('\nAll links: ', res3)

# Post
## 如果要以POST发送一个请求，只需要把参数data以bytes形式传入

# Handler
## 更复杂的控制
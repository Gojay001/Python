#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# beautifulsoup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen
# 基础
'''
url = 'https://morvanzhou.github.io/static/scraping/basic-structure.html'
html = urlopen(url).read().decode('utf-8')
#print(html)
# 以 lxml 形式加载进 BeautifulSoup
soup = BeautifulSoup(html, features='lxml')
print(soup.h1, '\n', soup.p)
# 获取  <a href="link"> 中 link
all_href = soup.find_all('a')
#print(all_href)
# 用 key 来读取 l["href"]
all_href = [l['href'] for l in all_href]
print('\n', all_href)
'''
# CSS
url2 = 'https://morvanzhou.github.io/static/scraping/list.html'
html = urlopen(url2).read().decode('utf-8')
print(html)
## 按 class 匹配
### 找所有 class=month 的信息
soup = BeautifulSoup(html, features='lxml')
month = soup.find_all('li', {"class": "month"})
for m in month:
	print(m.get_text())
### 找到 class=jan 的信息
jan = soup.find('ul', {"class": "jan"})
d_jan = jan.find_all('li')
for d in d_jan:
	print(d.get_text())

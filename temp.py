#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 加载库
from urllib import request
from urllib.parse import urlencode, quote
import json
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + \
    quote('热门') + '&sort=recommend&page_limit=20&page_start=0'

print(url)

req = request.Request(url)
response = request.urlopen(req, timeout=20)
result = response.read().decode('utf-8')
# 加载json为字典
result = json.loads(result)
print(result)

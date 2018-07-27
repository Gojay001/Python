#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba

jieba.load_userdict('/Users/gojay/Downloads/user.dict')
stop_words = '' # 停用词
with open('/Users/gojay/Downloads/stopword.dict', encoding='utf-8') as f:
    stop_words = f.read().split('\n')
# print(stop_words)
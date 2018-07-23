#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# snownlp_test.py

from snownlp import SnowNLP

# 测试
s = SnowNLP("我今天捡到100元人民币,真是太兴奋了")
print(s.words)  # 分词
tags = [x for x in s.tags]  # 词性标注
print(tags)
print(s.sentences)  # 断句
print(s.sentiments)  # 情绪判断(1为正面情绪，0为负面情绪)
print(s.pinyin)  # 拼音
print(s.han)  # 繁体转简体
print(s.keywords(limit=10))  # 关键词抽取
print(s.summary(limit=4))  # 概括总结文意
## 信息量衡量:TF-IDF(评价词对文本的重要性)
s1 = SnowNLP([['性格', '善良'],
              ['善良', '温柔', '温柔'],
              ['温柔', '善良'],
              ['好人'],
              ['性格', '善良']])
print(s1.tf)
print(s1.idf)
print(s1.sim(['温柔']))  # 文本相似性
print(s1.sim(['善良']))

# 分析文件评论情绪
with open('file1/jd_100.csv', 'r', encoding='gbk') as f:
    i = 0
    for fline in f.readlines():
        textjd = SnowNLP(fline)
        print(textjd.sentences, textjd.sentiments)
        print(textjd.keywords(limit=10))
        i += 1
        if i > 10:
            break
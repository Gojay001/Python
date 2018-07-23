#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# wordcloud_test.py

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

stopwords = {}


def importStopword(filename=''):
    global stopwords
    f = open(filename, 'r', encoding='utf-8')
    line = f.readline().rstrip()

    while line:
        stopwords.setdefault(line, 0)
        stopwords[line] = 1
        line = f.readline().rstrip()
    f.close()


def processChinese(textContent):
    jieba.enable_parallel(4)
    seg_generator = jieba.cut(textContent)  # 使用结巴分词，也可以不使用
    seg_list = [i for i in seg_generator if i not in stopwords]
    seg_list = [i for i in seg_list if i != u' ']
    seg_list = r' '.join(seg_list)
    return seg_list


importStopword(filename='file1/stopwords.txt')

# 获取当前文件路径
# __file__ 为当前文件, 在ide中运行此行会报错,可改为
# d = path.dirname('.')
d = path.dirname(__file__)

text = open(path.join(d, 'file1/jd_100.csv'), encoding='gbk').read()

# 如果是中文
text = processChinese(text)  # 中文不好分词，使用Jieba分词进行

# 设置背景图片
back_coloring = imread(path.join(d, "/Users/gojay/Downloads/china_map.png"))

wc = WordCloud(font_path="/Users/gojay/Downloads/msyh.ttf",  # 设置字体
               background_color="white",  # 背景颜色
               max_words=2000,  # 词云显示的最大词数
               #mask=back_coloring,  # 设置背景图片
               max_font_size=200,  # 字体最大值
               random_state=42,  # 设置有多少种随机生成状态，即有多少种配色方案
               )
# 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
wc.generate(text)
# wc.generate_from_frequencies(txt_freq)
# txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
# 从背景图片生成颜色值
# image_colors = ImageColorGenerator(back_coloring)
# 绘制词云
plt.figure()
# 以下代码显示图片
plt.imshow(wc)
plt.axis("off")
plt.show()

# 保存图片
wc.to_file(path.join(d, "file1/show1.png"))

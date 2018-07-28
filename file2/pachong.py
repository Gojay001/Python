import urllib.request
import json
import time
import random
import pymysql.cursors
import pandas as pd 

productNames = []
coms = []
contents = []
def crawlProductComment(url,page):

    #读取原始数据(注意选择gbk编码方式)
    html = urllib.request.urlopen(url).read().decode('gbk')

    #从原始数据中提取出JSON格式数据(分别以'{'和'}'作为开始和结束标志)
    jsondata = html[27:-2]
    #print(jsondata)
    data = json.loads(jsondata)

    #print(data['comments'])
    #print(data['comments'][0]['content'])
    #遍历商品评论列表
    for i in data['comments']:
        productName = i['referenceName']
        commentTime = i['creationTime']
        content = i['content']

        #输出商品评论关键信息
        print("商品全名:{}".format(productName))
        print("用户评论时间:{}".format(commentTime))
        print("用户评论内容:{}".format(content))
        print("-----------------------------")
        productNames.append(productName)
        coms.append(commentTime)
        contents.append(content)

        '''
        数据库操作
        '''

        # #获取数据库链接
        # connection  = pymysql.connect(host = 'localhost',
        #                           user = 'root',
        #                           password = '',
        #                           db = 'cmac',
        #                           charset = 'utf8mb4')
        # try:
        #     #获取会话指针
        #     with connection.cursor() as cursor:
        #         #创建sql语句
        #         sql = "insert into `jd-mi6` (`productName`,`commentTime`,`content`) values (%s,%s,%s)"

        #         #执行sql语句
        #         cursor.execute(sql,(productName,commentTime,content))

        #         #提交数据库
        #         connection.commit()
        # finally:
        #     connection.close()


for i in range(0,100):
    print("正在获取第{}页评论数据!".format(i+1))
    #小米6评论链接,通过更改page参数的值来循环读取多页评论信息
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv56668&productId=4335129&score=0&sortType=5&page=' + str(i) +'&pageSize=10&isShadowSku=0&fold=1'
    crawlProductComment(url,i)
    df2 = pd.DataFrame({'商品全名':productNames,'用户评论时间':coms,'用户评论内容':contents})
    df2.to_csv('a.csv')
    file_name = open('restxt.txt','w',encoding='utf-8')
    file_name.writelines(contents)
    file_name.close()
    #设置休眠时间
    # time.sleep(random.randint(31,33))
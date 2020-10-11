# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# 注册到settings.py文件的ITEM_PIPELINES中，激活组件
#from itemadapter import ItemAdapter


import  pymysql
class MaoyanmoviewPipeline:
    def __init__(self):
        self.connect=pymysql.connect(host='192.168.37.129',user='root',password='1qaz@WSX',db='testycc',port=3306)
        self.cursor=self.connect.cursor()

    def process_item(self, item, spider):
        movieTitle = item['movieTitle']
        movieType = item['movieType']
        movieTime = item['movieTime']

#  创建数据库
        # self.cursor.execute('''
        # create table MTable(
        # movieTitle varchar(255),
        # movieType varchar(255),
        # movieTime varchar(255))
        # ENGINE=InnoDB DEFAULT CHARSET=utf8'''
        # )


# 往数据库里面写入数据

        self.cursor.execute('insert into MTable values(%s,%s,%s)', (movieTitle, movieType, movieTime))
        # self.cursor.execute('select * from MTable')
        self.connect.commit()
        return item
    # 关闭数据库
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
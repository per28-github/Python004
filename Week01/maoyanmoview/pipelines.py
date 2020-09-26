# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# 注册到settings.py文件的ITEM_PIPELINES中，激活组件
#from itemadapter import ItemAdapter
class MaoyanmoviewPipeline:
#    def process_item(self, item, spider):
#        return item
    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        movieTitle = item['movieTitle']
        movieType = item['movieType']
        movieTime = item['movieTime']
        output = f'|{movieTitle}|\t|{movieType}|\t|{movieTime}|\n\n'
        with open('./maoyaninfo11222.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item

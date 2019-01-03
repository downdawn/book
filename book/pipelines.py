# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import pymongo

class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.collection
        # self.db[name].insert(dict(item))
        self.db[name].update({'book_url': item['book_url']}, dict(item), True)
        return item

    def close_spider(self, spider):
        self.client.close()

# class BookPipeline(object):
#
#     def __init__(self):#初始化
#         self.f=codecs.open('D:/jd.json','a',encoding= 'utf-8')
#     def process_item(self, item, spider):
#         # for j in range(0,len(item['book_name'])):#每页的商品总数为循环次数
#         book_name=item['book_name']#提取元素，以下同理
#         book_price=item['book_price']
#         book_img=item['book_img']
#         this_url=item['this_url']
#         g={'book_name':book_name,'book_price':book_price,'book_img':book_img,'this_url':this_url}#将提取的到的元素重新创建一个字典
#         i=json.dumps(dict(g),ensure_ascii= False )#设置json文件的编码
#         line=i+'\n'#每行后加换行
#         self.f.write(line)#写入文件
#         # return item
#     def close_spider(self):#关闭文件
#         self.f.close()


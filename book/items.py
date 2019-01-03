# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    collection = 'ddbook'

    b_cate = scrapy.Field()  # 大分类
    m_cate = scrapy.Field()  # 中分类
    s_href = scrapy.Field()  # 小分类地址
    s_cate = scrapy.Field()  # 小分类
    book_img = scrapy.Field()  # 图片
    book_name = scrapy.Field()  # 名字
    book_desc = scrapy.Field()  #
    book_author = scrapy.Field()  # 小作者
    book_press = scrapy.Field()  # 出版社
    book_publish_date = scrapy.Field()  # 出版日期
    book_sku = scrapy.Field()  # sku
    book_price = scrapy.Field()  # 价格
    this_url = scrapy.Field()  # 下一页地址
    book_url = scrapy.Field()  # 该书地址




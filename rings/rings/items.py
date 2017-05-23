# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field


class RingsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #id =        Field()
    name =   scrapy.Field()
    # text =      Field()
    #image =     Field()
    #url =       Field()
    #category =  Field()
    last_updated = scrapy.Field(serializer=str)


# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join

class IherbItem(scrapy.Item):
    title = scrapy.Field()          # Название, наименование продукта
    url = scrapy.Field()            # Адрес страницы продукта
    description = scrapy.Field()    # Описание продукта
    image = scrapy.Field()          # Фото продукта
    firma = scrapy.Field()          # Название производителя
    price = scrapy.Field()          # Цена товара

class IherbItemLoader(ItemLoader):
    url_out = TakeFirst()
    title_out = TakeFirst()
    # description_in = Join()
    description_out = TakeFirst()
    image_out = TakeFirst()
    firma_out = TakeFirst()
    price_out = TakeFirst()

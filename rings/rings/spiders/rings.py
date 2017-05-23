from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from rings.items import RingsItem

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
book = {}

class RingsSpader(scrapy.Spider):
    name = 'jewels'
    # allowed_domains = ['rings.su']
    start_urls = ['https://ru.iherb.com/pr/Country-Life-Acetyl-L-Carnitine-Caps-500-mg-240-Veggie-Caps/8523']

    def parse(self, response):
        SET_SELECTOR = '.image-container'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'img::attr(alt)'
            IMAGE_SELECTOR = 'img::attr(src)'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }
        SET_SELECTOR1 = '.inner-content'
        for brickset in response.css(SET_SELECTOR1):
            DESCRIPTION_SELECTOR = 'div ::text'
            yield {
                'text': brickset.css(DESCRIPTION_SELECTOR).extract(),
            }
    # rules = (
    # rules = (

    #     Rule(SgmlLinkExtractor(allow=('catalog.+')), follow=True),
    #     Rule(SgmlLinkExtractor(allow=('goods.+')), callback='parse_item'),
    # )

    # def parse_item(self, response):
    #     # hxs = HtmlXPathSelector(response)
    #     # l = RingsLoader(RingsItem(), hxs)
    #     l = RingsLoader(item=RingsItem(), response=response)
    #     # l.add_xpath('name', "\<h1 itemprop\=\"name\"\>(.+)\<\/h1\>")
    #     l.add_xpath('name', "<h1 itemprop=\"name\">(.+)\</h1>")
    #     # l.add_xpath('text', "<h1 itemprop=\"name\">(.+)<\/h1>")
    #
    #
    #     l.add_value('url', response.url)
    #
    #     return l.load_item()

    # def parse_item(self, response):
    #     self.logger.info('Hi, this is an item page! %s', response.url)
    #     item = scrapy.Item()
    #     # item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
    #     item['name'] = response.xpath('<h1 [@itemprop="name"]>text(.+)\</h1>').extract()
    #     # item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
    #     return item

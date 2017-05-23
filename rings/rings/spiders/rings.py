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

class ToScrapeCSSSpider(scrapy.Spider):
    name = "rings"
    start_urls = [
        'https://sale.aliexpress.com/ru/mall_best.htm?spm=a2g02.8319747.j-mall-header.8.33TsbO',
    ]

    def parse(self, response):
        for quote in response.css("div.item-box"):
            yield {
                'text': quote.css("div.detail-box ::attr(title)").extract_first(),
                'image': quote.css("div.image-box img::attr(src)").extract_first(),
                'price': quote.css("div.price a.tag::text").extract_first()
            }

        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))

import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from iherb.items import IherbItemLoader, IherbItem

class IherbSpider(CrawlSpider):
    name = 'iherb'
    allowed_domains = ['ru.iherb.com']
    start_urls = ['https://ru.iherb.com/c']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//div[@class="panel-stack"]/div[@class="panel"]', '//div[@class="pagination"]/a[@class="pagination-next"]'],
                allow='https://ru.iherb.com/pr/.+\d+',
            ), callback='parse_item'
        ),
        Rule(
            LinkExtractor(
                restrict_xpaths=['//div[@class="pagination"]/a[@class="pagination-next"]'],
                allow='https://ru.iherb.com/c.+',
            ), follow=True
        ),
    )

    def parse_item(self, response):
        selector = Selector(response)
        l = IherbItemLoader(IherbItem(), selector)
        l.add_value('url', response.url)
        # l.add_xpath('title', '//section[@class="column fluid product-description-title hidden-xs hidden-sm"]/div[@id="product-summary-header"]/h1[@id="name"]/text()')
        # l.add_xpath('description', '//div[@class="inner-content"]/div[@class="item-row"][1]/text()')
        # l.add_xpath('image', '//div[@class="thumbnail-container"]/img[@class="selected"]/@src')
        # l.add_xpath('firma', '//section[@class="column fluid product-description-title hidden-xs hidden-sm"]/div[@id="product-summary-header"]/div[@id="brand"]/a/span/bdi/text()')
        return l.load_item()

# scrapy crawl iherb -o scarped_data_utf8.json -t json

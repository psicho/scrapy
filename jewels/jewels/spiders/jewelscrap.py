from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from jewels.items import JewelsItem


class JewelsLoader(XPathItemLoader):
    default_output_processor = TakeFirst()

class JewelSpader(CrawlSpider):
    name = "jewels"
    allowed_domains = ["rings.su"]
    start_urls = ["http://rings.su/catalog"]

    rules = (
        Rule(SgmlLinkExtractor(allow=('act=catalog')), follow=True),
        Rule(SgmlLinkExtractor(allow=('act=goods')), callback='parse_item'),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        l = JewelsLoader(JewelsItem(), hxs)
        l.add_xpath('id', "//td[text()='%s']/following-sibling::td/text()" % u"Рег. номер:")
        l.add_value('url', response.url)
        return l.load_item()
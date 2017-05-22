from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from rings.items import RingsItem


class RingsLoader(XPathItemLoader):
    default_output_processor = TakeFirst()

class RingsSpader(CrawlSpider):
    name = "jewels"
    allowed_domains = ["rings.su"]
    start_urls = ["http://rings.su/catalog"]

    rules = (
        Rule(SgmlLinkExtractor(allow=('catalog.+')), follow=True),
        Rule(SgmlLinkExtractor(allow=('goods.+')), callback='parse_item'),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        l = RingsLoader(RingsItem(), hxs)
        l.add_xpath('name', "\<h1 itemprop\=\"name\"\>(.+)\<\/h1\>")
        # l.add_xpath('text', "<h1 itemprop=\"name\">(.+)<\/h1>")


        l.add_value('url', response.url)

        return l.load_item()
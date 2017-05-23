from scrapy import Selector

sel = Selector(text='<div class="hero shout"><time datetime="2014-07-23 19:00">Special date</time></div>')

sel.css('.shout').xpath('./time/@datetime').extract()
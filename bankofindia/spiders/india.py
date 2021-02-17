import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from bankofindia.items import Article


class IndiaSpider(scrapy.Spider):
    name = 'india'
    start_urls = ['https://www.bankofindia.co.in/']

    def parse(self, response):

        articles = response.xpath('//li[@class="UpcomingSessions-box"]')
        for article in articles:
            item = ItemLoader(Article())
            item.default_output_processor = TakeFirst()
            title = article.xpath('.//a/text()').get()
            if title:
                title = title.strip()
            else:
                return

            link = response.urljoin(article.xpath('.//a/@href').get())
            if 'https' not in link:
                return

            item.add_value('title', title)
            item.add_value('link', link)

            yield item.load_item()

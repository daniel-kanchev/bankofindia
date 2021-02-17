import scrapy


class Article(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()

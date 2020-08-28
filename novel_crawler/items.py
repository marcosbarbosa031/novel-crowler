import scrapy


class NovelChapterItem(scrapy.Item):
    novel = scrapy.Field()
    title = scrapy.Field()
    number = scrapy.Field()
    link = scrapy.Field()
    body = scrapy.Field()


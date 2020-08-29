import scrapy

class NovelChapterItem(scrapy.Item):
    novel = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    body = scrapy.Field()

    def __repr__(self):
        return repr({
            'novel': self['novel'],
            'title': self['title'],
            'link': self['link']
        })


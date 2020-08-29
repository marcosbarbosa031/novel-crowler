import scrapy

class NovelChapterItem(scrapy.Item):
    novel = scrapy.Field()
    chapter = scrapy.Field()
    link = scrapy.Field()
    body = scrapy.Field()

    def __repr__(self):
        return repr({
            'novel': self['novel'],
            'chapter': self['chapter'],
            'link': self['link']
        })


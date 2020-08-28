import scrapy
from novel_crawler.items import NovelChapterItem

class ReadlightnovelsSpider(scrapy.Spider):
    name = 'ReadLightNovels'
    allowed_domains = ['readlightnovels.net']
    start_urls = ['https://readlightnovels.net/only-i-level-up.html']

    def parse(self, response):
        for chapters in response.css('ul.list-chapter li'):
            link = chapters.css("a::attr(href)").extract_first()

            yield response.follow(link, self.parse_chapter)
        
    def parse_chapter(self, response):
        link = response.url
        novel = response.css("a.truyen-title::text").extract()
        title = response.css("a.chapter-title::text").extract()
        text = response.css("div.chapter-content").extract()

        chapter = NovelChapterItem(novel = novel[0], title = title[0], link = link, text = text[0])

        yield chapter

import scrapy, re, json, os, io, pdfkit

from novel_crawler.items import NovelChapterItem

class ReadlightnovelsSpider(scrapy.Spider):
    name = 'ReadLightNovels'
    allowed_domains = ['readlightnovels.net']
    start_urls = ['https://readlightnovels.net/only-i-level-up.html']
    chapter_url = 'https://readlightnovels.net/only-i-level-up/$.html'
    template = ''
    page = 1

    def parse(self, response):
        with io.open('template/template.html', 'r', encoding='utf-8') as f:
            self.template = f.read()
        
        for chapters in response.css('ul.list-chapter li'):
            link = chapters.css('a::attr(href)').extract_first()

            yield response.follow(link, self.parse_chapter)
        
        self.page += 1

        next_page = response.css(f'ul.pagination-sm li a[data-page*="{self.page}"]::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        
    def parse_chapter(self, response):
        link = response.url
        novel = response.css('a.truyen-title::text').extract_first()
        title = response.css('a.chapter-title::text').extract_first()
        body = response.css('div.chapter-content').extract_first()

        chapter = NovelChapterItem(novel = novel, title = title, link = link, body = body)

        self.save_pdf(body, title)

        yield chapter

    def save_pdf(self, body, title):
        if not os.path.exists('Novels/Solo Leveling/'):
            os.makedirs(os.path.dirname('Novels/Solo Leveling/'))
        
        
        with io.open(f'Novels/Solo Leveling/{title}.html', 'w', encoding='utf-8') as f:
            f.write(self.template.replace('${content}', body))
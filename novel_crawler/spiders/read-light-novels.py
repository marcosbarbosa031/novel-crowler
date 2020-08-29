import scrapy, os, json

from scrapy.http import FormRequest, HtmlResponse
from novel_crawler.items import NovelChapterItem

class ReadlightnovelsSpider(scrapy.Spider):
    name = 'ReadLightNovels'
    allowed_domains = ['readlightnovels.net']
    start_urls = ['https://readlightnovels.net/only-i-level-up.html']
    novel = ''
    page = 1

    def parse(self, response):
        html = self.get_pagination_content(response) if self.page > 1 else response

        for chapters in html.css('ul.list-chapter li'):
            link = chapters.css('a::attr(href)').extract_first()
            yield html.follow(link, self.parse_chapter)
        
        self.page += 1

        next_page_url = html.css(f'ul.pagination-sm li a[data-page*="{self.page}"]::attr(href)').extract_first()
        print('PAGINATION: ', next_page_url);
        if next_page_url is not None:
            yield self.go_to_next_page()
        
    def parse_chapter(self, response):
        link = response.url
        self.novel = response.css('a.truyen-title::text').extract_first()
        chapter = response.css('a.chapter-title::text').extract_first()
        body = response.css('div.chapter-content').extract_first()

        chapter = NovelChapterItem(novel = self.novel, chapter = chapter, link = link, body = body)
        yield chapter

    def go_to_next_page(self):
        formdata = {
            'action': 'tw_ajax',
            'type': 'pagination',
            'id': '256775',
            'page': f'{self.page}',
        }
        pagination_url = 'https://readlightnovels.net/wp-admin/admin-ajax.php'
        return FormRequest(pagination_url, callback = self.parse, formdata = formdata)
    
    def get_pagination_content(self, response):
        json_pagination = json.loads(response.text)
        body = json_pagination['list_chap'] + json_pagination['pagination']
        return HtmlResponse(url = self.start_urls[0], body = body, encoding = 'utf-8')

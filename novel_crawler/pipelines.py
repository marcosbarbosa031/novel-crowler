import os, io
from xhtml2pdf import pisa

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class NovelCrawlerPipeline:
    template = ''

    def open_spider(self, spider):
        with io.open('template/template.html', 'r', encoding='utf-8') as f:
            self.template = f.read()

    def process_item(self, item, spider):
        self.save_pdf(item)
        return item
    
    def save_pdf(self, item):
        novel = item['novel']
        chapter = self.remove_invalid_characters_from_path(item['chapter'])

        if not os.path.exists(f"Novels/{novel}/"):
            os.makedirs(os.path.dirname(f"Novels/{novel}/"))

        with open(f"Novels/{novel}/{chapter}.pdf", 'w+b') as pdf_file:
            pisa.CreatePDF(
                self.template.replace('${content}', item['body']),
                dest = pdf_file
            )

    def remove_invalid_characters_from_path(self, path):
        invalid_characters = '\/:*?"<>|'
        for char in invalid_characters:
            path = path.replace(char, '')
        return path

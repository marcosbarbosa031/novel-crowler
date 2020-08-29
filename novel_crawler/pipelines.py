import os, io
from xhtml2pdf import pisa

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class NovelCrawlerPipeline:
    template = ''

    def open_spider(self, spider):
        with io.open('template/template.html', 'r', encoding='utf-8') as f:
            self.template = f.read()
        
        if not os.path.exists(f'Novels/Solo Leveling Novel (Only I Level Up Novel)/'):
            os.makedirs(os.path.dirname(f'Novels/Solo Leveling Novel (Only I Level Up Novel)/'))

    def process_item(self, item, spider):
        self.save_pdf(item)
        return item
    
    def save_pdf(self, item):
        pdf_file = open(f"Novels/{item['novel']}/{item['chapter']}.pdf", 'w+b')

        status = pisa.CreatePDF(
            self.template.replace('${content}', item['body']),
            dest = pdf_file
        )

        pdf_file.close()

# novel-crowler

A simple Web Crawler, made in Python with Scrapy, to download light novel chapters in PDF (styled for Kindle).
from readlightnovels.net.

# Installing requirements

Install the required packages runing
```
pip install -r requirements.txt
```


# Runing the crawler

Downloading Web Novel chapters from readlightnovels.net passing the novel url as an argument
```
scrapy crawl WebNovel -a url=https://readlightnovels.net/the-mech-touch.html
```

It will download the chapters in PDF on the following dirrectory
```
Novels/*Novel Name*/
```

# novel-crowler

A simple Web Crawler, made in Python with Scrapy, to download light novel chapters in PDF (styled for Kindle).
At the moment only downloading Solo Leveling chapters.

# Installing requirements

Install the required packages runing
```
pip install -r requirements.txt
```


# Runing the crawler

Downloading Web Novel chapters from readlightnovels.net passing the novel url as an argument
```
scrapy crawl WebNovel -a url=https://readlightnovels.net/only-i-level-up.html
```

It will download the chapters in PDF on the following dirrectory
```
Novels/Solo Leveling Novel (Only I Level Up Novel)/
```

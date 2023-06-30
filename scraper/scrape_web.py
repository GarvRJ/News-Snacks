from time import mktime

from objects.snacks import Snack
from processor.paraphraser import sent_paraphraser, paraphraser
from processor.summarizer import summarizer
from scraper.get_rss import get_links
from newspaper import Article
import feedparser
from _datetime import datetime, timedelta
from objects.content import Content


def latest_article_links():
    urls = get_links()
    current_time = datetime.now()

    threshold = current_time - timedelta(hours=8)

    print('Finding new articles in these sources...')
    links = []
    for url in urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if "published_parsed" in entry:
                published_date = datetime.fromtimestamp(mktime(entry.published_parsed))
            else:
                pass
            if published_date >= threshold:
                link = entry.link
                links.append(link)

    print('Found ' + str(len(links)) + ' new articles')
    return links


def scrape_web():
    content = []
    links = latest_article_links()
    print('Scraping those articles...')
    for link in links:
        try:
            article = Article(str(link))
            article.download()
            article.parse()
            article_title = str(sent_paraphraser(str(article.title)))
            article_text = str(paraphraser(str(summarizer(str(article.text)))))
            article_tags = article.tags
            image = article.top_image
            print(str(image))
            article_time = article.publish_date
            snack = Snack(name=article_title, description=article_text, link= link, time= article_time)
            snack.add()
        except:
            pass
    return content

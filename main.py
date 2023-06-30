import time

from objects.snacks import Snack
from processor.paraphraser import paraphraser, sent_paraphraser
from processor.summarizer import summarizer
from scraper.scrape_web import scrape_web

if __name__ == '__main__':
    start = time.time()
    print("Starting service...")
    data = scrape_web()
    end = time.time()
    time = (end - start)
    print(str(time))
    # for article in data:
    #     description = summarizer(article.content)
    #     description = paraphraser(description)
    #     title = sent_paraphraser(article.title)
    #     tstamp = article.timestamp
    #     link = article.link
    #     snack = Snack(name=title, description=description, time=tstamp, link=link)
    #     snack.add()

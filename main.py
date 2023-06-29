from urllib.parse import urlparse

from objects.snacks import Snack
from processor.paraphraser import paraphraser, sent_paraphraser
# from processor.paraphraser_new import paraphrase_paragraph, paraphrase_sentence
from processor.summarizer import summarizer
from scraper.scrape_web import scrape_web
if __name__ == '__main__':
    data = scrape_web()
    snacks = []
    for article in data:
        description = summarizer(article.content)
        description = paraphraser(description)
        title = sent_paraphraser(article.title)
        tstamp = article.timestamp
        link = article.link
        snacks.append(Snack(name=title, description=description,time=tstamp, link=link))
    for snack in snacks:
        snack.print()

import math
from time import mktime
import threading
from objects.snacks import Snack
from processor.paraphraser import sent_paraphraser, paraphraser
from processor.summarizer import summarizer
from scraper.get_rss import get_links
# noinspection PyPackageRequirements
from newspaper import Article
import feedparser
from _datetime import datetime, timedelta


def latest_article_links():
    urls = get_links()
    current_time = datetime.now()

    threshold = current_time - timedelta(hours=48)

    print('Finding new articles in these sources...')
    links = []
    for url in urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if "published_parsed" in entry:
                published_date = datetime.fromtimestamp(mktime(entry.published_parsed))
            else:
                published_date = datetime.fromtimestamp(0)
            if published_date >= threshold:
                link = entry.link
                links.append(link)

    print('Found ' + str(len(links)) + ' new articles')
    return links


def split(list_a, chunk_size):
    list_b = []
    for i in range(0, len(list_a), chunk_size):
        list_b.append(list_a[i:i + chunk_size])

    return list_b


# noinspection PyBroadException
def scrape_article(**kwargs):
    for link in kwargs['thread_list']:
        try:
            article = Article(str(link))
            article.download()
            article.parse()
            article_title = str(sent_paraphraser(str(article.title)))
            article_text = str(paraphraser(str(summarizer(str(article.text)))))
            # article_tags = article.tags
            # TODO: Add tagging feature for articles for better SEO.
            image = str(article.top_image)
            print(image)
            article_time = article.publish_date
            snack = Snack(name=article_title, description=article_text, link=link, time=article_time, image_link=image)
            snack.print()
            snack.add()
        except:
            pass


def scrape_web():
    links = latest_article_links()
    chunk_size = math.ceil(len(links) / 16)
    threads = split(links, chunk_size)
    t1 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[0]})
    t2 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[1]})
    t3 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[2]})
    t4 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[3]})
    t5 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[4]})
    t6 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[5]})
    t7 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[6]})
    t8 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[7]})
    t9 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[8]})
    t10 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[9]})
    t11 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[10]})
    t12 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[11]})
    t13 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[12]})
    t14 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[13]})
    t15 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[14]})
    t16 = threading.Thread(target=scrape_article, kwargs={'thread_list': threads[15]})
    print('Scraping those articles...')
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()

from bs4 import BeautifulSoup as bs4
import requests
import feedparser
import urllib.parse

from init_setup.creds import fetch_links, key, save_rss


response = requests.post(fetch_links, data={"key": key})


def find_feed(source):
    print(source)
    raw = requests.get(source).text
    result = []
    possible_feeds = []
    html = bs4(raw)
    feed_urls = html.findAll("link", rel="alternate")
    if len(feed_urls) > 1:
        for f in feed_urls:
            t = f.get("type", None)
            if t:
                if "rss" in t or "xml" in t:
                    href = f.get("href", None)
                    if href:
                        possible_feeds.append(href)
    parsed_url = urllib.parse.urlparse(source)
    base = parsed_url.scheme + "://" + str(parsed_url.hostname)
    atags = html.findAll("a")
    for a in atags:
        href = a.get("href", None)
        if href:
            if "xml" in href or "rss" in href or "feed" in href:
                possible_feeds.append(base + href)
    for url in list(set(possible_feeds)):
        f = feedparser.parse(url)
        if len(f.entries) > 0:
            if url not in result:
                result.append(url)
    if not result:
        result = 'not found'
    print(result)
    return result


dt = {}

if response.status_code == 200:
    sites = []
    # Extract the list data from the response
    sequence = response.json()
    for link in sequence:
        sites.append(link["source_link"])
elif response.status_code == 403:
    # Print an error message if the request failed
    print("Request failed due to invalid key:", response.status_code)
    sites = []
else:
    print("Request failed with status code:", response.status_code)
    sites = []

count = 1
print(len(sites))
for site in sites:
    save = requests.post(save_rss, data={"key": key, "site": site, "rss": find_feed(site)})
    print(save.text)

import requests
from urllib.parse import urlparse
from init_setup.creds import add_article, key


class Snack:
    def __init__(self, name, description, time, link, image_link):
        self.name = str(name)
        self.description = str(description)
        self.time = str(time)
        self.link = str(link)
        self.source_name = str(urlparse(link).hostname)
        self.image_link = str(image_link)
    def add(self):
        print("Uploading snacks...")
        response = requests.post(add_article, data={'key': key, 'title': self.name, 'description': self.description,
                                                    'link': self.link, 'source_name': self.source_name,
                                                    'time': self.time, 'image_link': self.image_link})
        print(response.text)

    def print(self):
        print("Title: \t\t\t" + self.name)
        print("Description: \t" + str(self.description))
        print("Time: \t\t\t" + str(self.time))
        print("Image Link: \t\t\t" + str(self.image_link))
        print("Link: \t\t\t" + str(self.link))
        print("Source: \t\t\t" + str(self.source_name) + "\n")

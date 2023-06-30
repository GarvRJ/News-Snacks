import time


class Content:
    timestamp = time.time()

    def __init__(self, title, link, content, tags, timestamp):
        self.title = title
        self.link = link
        self.content = content
        self.timestamp = timestamp
        self.tags = tags

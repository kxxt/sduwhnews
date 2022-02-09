class BaseCrawler:
    def __init__(self):
        self.data = []
        self.initialized = False
        pass

    def crawl(self):
        pass

    def __iter__(self):
        if not self.initialized:
            self.crawl()
            self.initialized = True
        return iter(self.data)
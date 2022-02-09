from itertools import chain


class BaseCrawler:
    def __init__(self):
        self.data = []
        self.initialized = False
        self.__errors = []
        pass

    def crawl(self):
        pass

    def __iter__(self):
        if not self.initialized:
            self.crawl()
            self.initialized = True
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    @property
    def errors(self):
        return iter(self.__errors)

    def _add_error(self, error):
        self.__errors.append(error)

    def _add_index_error(self, url):
        self._add_error(f"FATAL: Failed to get {url}")

    def _add_item_error(self, url, item):
        self._add_error(f"WARN: one failed item on {url}: {str(item)}")


class AggregatedCrawler(BaseCrawler):
    def __init__(self, *crawlers):
        super().__init__()
        self.crawlers = crawlers

    def crawl(self):
        for crawler in self.crawlers:
            crawler.crawl()

    def __iter__(self):
        if not self.initialized:
            self.crawl()
            self.initialized = True
        return chain(*(crawler for crawler in self.crawlers))

    def __len__(self):
        return sum(len(crawler) for crawler in self.crawlers)

    @property
    def errors(self):
        return chain(*(crawler.errors for crawler in self.crawlers))

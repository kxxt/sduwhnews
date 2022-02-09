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
        return self.__errors

    def _add_error(self, error):
        self.__errors.append(error)


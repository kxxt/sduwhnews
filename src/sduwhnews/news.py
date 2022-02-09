class News:
    def __init__(self, title, url, date):
        self.title = title
        self.url = url
        self.date = date

    def __repr__(self):
        return f'{self.title}\n{self.date}\n{self.url}'


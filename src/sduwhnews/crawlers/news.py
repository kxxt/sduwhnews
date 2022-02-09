import requests
from .base import BaseCrawler
from ..constants import SDUWH_NEWS_URL, SDUWH_NEWS_ROOT_URL
from ..news import News
from bs4 import BeautifulSoup


class NewsCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()
        self.index_url = SDUWH_NEWS_URL

    def crawl(self):
        response = requests.get(self.index_url)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            news_list = soup.select('.n_newslist li')
            for news in news_list:
                a = news.find('a')
                span = news.find('span')
                if a and span:
                    title = a.attrs['title']
                    url = a.attrs['href']
                    if not url.startswith('http'):
                        url = SDUWH_NEWS_ROOT_URL + url
                    date = span.text
                    news = News(title, url, date)
                    self.data.append(news)
                else:
                    self._add_item_error(self.index_url, news)
        else:
            self._add_index_error(self.index_url)

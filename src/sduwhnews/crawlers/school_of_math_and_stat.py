import requests
from .base import BaseCrawler
from ..constants import SDUWH_MATH_URL_NEWS, SDUWH_MATH_URL_UNDERGRADUATE, \
    SDUWH_MATH_URL_ANNOUNCEMENT
from ..news import News
from bs4 import BeautifulSoup, Comment
from urllib.parse import urljoin


class MathCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()
        self.index_urls = [SDUWH_MATH_URL_NEWS, SDUWH_MATH_URL_ANNOUNCEMENT, SDUWH_MATH_URL_UNDERGRADUATE]

    def crawl(self):
        for index_url in self.index_urls:
            response = requests.get(index_url)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                news_list = soup.select('.list_r li')
                for news in news_list:
                    a = news.find('a')
                    span = news.find('span')
                    # Try to extract category
                    comments = news.find_all(text=lambda x: isinstance(x, Comment))
                    if comments:
                        category = BeautifulSoup(comments[0], "html.parser").text.strip()
                    else:
                        category = ''
                    if a and span:
                        title = category + a.attrs['title']
                        url = a.attrs['href']
                        if not url.startswith('http'):
                            url = urljoin(index_url, url)
                        date = span.text
                        news = News(title, url, date)
                        self.data.append(news)
                    else:
                        self._add_item_error(index_url, news)
            else:
                self._add_index_error(index_url)

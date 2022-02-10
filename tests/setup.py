import sys
from typing import Callable
import validators

sys.path.append("src")

from sduwhnews import *
from sduwhnews.crawlers.common import BaseCrawler


def is_null_or_empty(s: str) -> bool:
    return s is None or len(s.strip()) == 0


def make_crawler_test(func: Callable[[], BaseCrawler]) -> Callable[[], None]:
    def wrapper():
        c = func()
        c.crawl()
        assert len(c) > 0
        assert list(c.errors) == []
        for news in c:
            assert isinstance(news, News)
            assert not is_null_or_empty(news.title)
            assert not is_null_or_empty(news.date)
            assert validators.url(news.url)

    return wrapper

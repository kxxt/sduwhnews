import pickle
import os
from time import sleep

from telegram import Bot
import logging
from sduwhnews import *


def throw_helper(obj):
    raise obj


TOKEN = os.environ['TG_TOKEN'] or throw_helper('TG_TOKEN not set')
TG_CHAT_ID = os.environ['TG_CHAT_ID'] or throw_helper('TG_CHAT_ID not set')

bot = Bot(token=TOKEN)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def fatal_error(reason):
    try:
        bot.send_message(chat_id=TG_CHAT_ID, text=f"Bot fatal error: {reason}")
    except Exception as e:
        logging.error(
            f"Fatal error: {reason}.\n" +
            f"Another error arises while trying to send the previous error to channel.\n Error: {e}"
        )
    exit(1)


if __name__ == '__main__':
    crawled = set()
    try:
        if os.path.isfile('crawled.set'):
            with open('crawled.set', 'rb') as f:
                crawled = pickle.load(f)
        crawler = AggregatedCrawler(NewsCrawler(), OfficeOfEduAdminCrawler(), MathCrawler())
        for news in crawler:
            if news.url in crawled:
                continue
            crawled.add(news.url)
            bot.send_message(chat_id=TG_CHAT_ID, text=str(news))
            sleep(3.2)
    except Exception as e:
        fatal_error(e)
    finally:
        with open('crawled.set', 'wb') as f:
            pickle.dump(crawled, f)

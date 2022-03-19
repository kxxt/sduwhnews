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
    logging.info("sduwhnews/tgbot encountered FATAL error!")
    logging.error(f"FATAL ERROR: {reason}")
    try:
        bot.send_message(chat_id=TG_CHAT_ID, text=f"Bot fatal error: {reason}")
    except Exception as e:
        logging.error(f"Another error arises while trying to send the previous error to channel.\n Error: {e}")
    exit(1)


if __name__ == '__main__':
    logging.info("sduwhnews/tgbot started!")
    crawled = set()
    try:
        if os.path.isfile('crawled.set'):
            with open('crawled.set', 'rb') as f:
                crawled = pickle.load(f)
        crawler = AggregatedCrawler(NewsCrawler(), OfficeOfEduAdminCrawler(), MathCrawler())
        for news in crawler:
            if news.url in crawled:
                continue
            logging.info(f"Found new news: {news.url}")
            crawled.add(news.url)
            try:
                bot.send_message(chat_id=TG_CHAT_ID, text=str(news))
            except Exception as e:
                crawled.remove(news.url)
                logging.error(f"Error while sending news to channel.\n Error: {e}")
            sleep(3.2)
        logging.info("sduwhnews/tgbot finished successfully!")
    except Exception as e:
        fatal_error(e)
    finally:
        with open('crawled.set', 'wb') as f:
            pickle.dump(crawled, f)

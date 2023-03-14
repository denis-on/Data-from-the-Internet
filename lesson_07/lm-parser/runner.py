from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from lm-parser import settings
from lm-parser.spiders.leroymerlin import LeroymerlinSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    # key = input('Введите ключ: ')
    process.crawl(LeroymerlinSpider, text='линолиум')

    process.start()

import time

import schedule
from scrapy import cmdline
from scrapy.crawler import CrawlerProcess

# from .check_ip import CheckIPSpider


def run_spider_cmd():
    print("Running spider")
    cmdline.execute("scrapy crawl checkip".split())


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
})


schedule.every(3000).seconds.do(run_spider_cmd)

while True:
    schedule.run_pending()
    time.sleep(1)

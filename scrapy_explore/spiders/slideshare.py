import scrapy


class SlideshareSpider(scrapy.Spider):
    name = 'slideshare'
    allowed_domains = ['www.slideshare.net']
    start_urls = ['http://www.slideshare.net/']

    def parse(self, response):
        print('runing . . .')

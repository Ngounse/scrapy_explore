import scrapy


class FreeSpider(scrapy.Spider):
    name = 'checkip'
    allowed_domains = ['http://httpbin.org/']
    
    def start_requests(self):
        print('free ::: ')
        for i in range(10):
            ip = scrapy.Request(url='http://httpbin.org/ip?i='+str(i))
            yield ip

    def parse(self, response):
        item = dict([])
        print(response.text)
        item['ip'] = response.text
        yield item

import scrapy


class LeruaparserSpider(scrapy.Spider):
    name = "LeruaParser"
    allowed_domains = ["https://leroymerlin.ru"]
    start_urls = ["https://leroymerlin.ru/catalogue/osveshchenie/?page=1"]

    def parse(self, response):
        pass

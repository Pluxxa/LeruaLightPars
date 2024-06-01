import scrapy



class LParsSpider(scrapy.Spider):
    name = "l_pars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet/page-1"]
    custom_settings = {
        'FEEDS': {
            'output.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': None,
                'indent': 4,
            },
        }
    }

    def parse(self, response):
        lights = []
        try:
            links = []
            link = response.css('div.ui-jDl24')
            for i in link.css('a::attr(href)'):
                if len(links) == 0:
                    links.append(i)
                else:
                    flag = True
                    for j in links:
                        if i == j:
                            flag = False
                        else:
                            continue
                    if flag:
                        links.append(i)
                    else:
                        continue
            l = links[:-1]
            print(*links, sep='\n')
            print()
            print(*l, sep='\n')
        except IndexError:
            return 0


    #next_page = response.css('a.next::attr(href)').get()



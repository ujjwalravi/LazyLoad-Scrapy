import scrapy
import json

class LazyLoad(scrapy.Spider):
    name = "lazyload"
    page = 1
    start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']


    def parse(self, response):
        #for word in response.css(" h4.card-title > a::text"):
            #print(word.get())                        #I only want to print product name
        #m=2
        #nextPage = "https://scrapingclub.com/exercise/list_infinite_scroll/"+"?page="+str(m)
        #nextPage = response.css("a.next-page::attr('href')").get()
        #nextPage = "https://scrapingclub.com/exercise/list_infinite_scroll/"+ nextPage
        #print(nextPage)
        #if nextPage is not None:
            #response.follow(nextPage, self.parse)
            data=json.loads(response.text)
            for quote in data["quotes"]:
                print(quote)
                yield {"quote": quote["text"]}
            if data["has_next"]:
                self.page += 1
                #url = "http://quotes.toscrape.com/api/quotes?page={}".format(self.page)
                url = "http://quotes.toscrape.com/api/quotes?page="+str(self.page)
                yield scrapy.Request(url=url, callback=self.parse)

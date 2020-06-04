import scrapy


class LazyLoad(scrapy.Spider):
    name = "lazyload"
    start_urls = ['https://scrapingclub.com/exercise/list_infinite_scroll/']


    def parse(self, response):
        for word in response.css(" h4.card-title > a::text"):
            print(word.get())                        #I only want to print product name
        #m=2
        #nextPage = "https://scrapingclub.com/exercise/list_infinite_scroll/"+"?page="+str(m)
        nextPage = response.css("a.next-page::attr('href')").get()
        nextPage = "https://scrapingclub.com/exercise/list_infinite_scroll/"+ nextPage
        print(nextPage)
        if nextPage is not None:
            response.follow(nextPage, self.parse)

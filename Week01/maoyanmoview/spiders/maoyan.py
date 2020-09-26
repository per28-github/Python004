# -*- coding: utf-8 -*-
import scrapy
from maoyanmoview.items import MaoyanmoviewItem
# from bs4 import BeautifulSoup
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # start_urls = ['http://maoyan.com/']
    start_urls = ['https://maoyan.com/films?showType=3']


    # def parse(self, response):
    #     pass 
    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url,callback=self.parse)

        # for i in range(1,10):
        #     url = f'https://maoyan.com/films?showType=3'
        #     yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,reponse):
        print(reponse.url)
        print(reponse.text)
        movies = Selector(response=reponse).xpath('//div[@class="movie-item-hover"]')
        # for movie in movies:
        for movie in movies[0:10]:
            item = MaoyanmoviewItem()
            movieTitle = movie.xpath('./a/div/div[1]/span[1]/text()[1]')
            movieType = movie.xpath('./a/div/div[2]/text()[2]')
            movieTime = movie.xpath('./a/div/div[4]/text()[2]')
            print('-----44444444444------')
            print("标题。。。。",movieTitle)
            print("类型。。。。",movieType)
            print("上映时间",movieTime)
            print('-----555555555------')
            print("标题。。。。",movieTitle.extract())
            print("类型。。。。",movieType.extract())
            print("上映时间...",movieTime.extract())
            print('-----55666666666666666666665555555------')
            print('movieTitle',movieTitle.extract_first())
            print('movieType',movieType.extract_first())
            print('movieTime',movieTime.extract_first())
            item['movieTitle'] = movieTitle.extract_first()
            item['movieType'] = movieType.extract_first()
            item['movieTime'] = movieTime.extract_first()
            # item['movieTime'] = ''.join(item['movieTime'].split())
            yield item
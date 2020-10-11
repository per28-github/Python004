# -*- coding: utf-8 -*-
import scrapy
from maoyanmoview.items import MaoyanmoviewItem
# from bs4 import BeautifulSoup
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,reponse):
        print(reponse.url)
        print(reponse.text)
        movies = Selector(response=reponse).xpath('//div[@class="movie-item-hover"]')
        try:
            for movie in movies[0:10]:
                item = MaoyanmoviewItem()
                movieTitle = movie.xpath('./a/div/div[1]/span[1]/text()[1]')
                movieType = movie.xpath('./a/div/div[2]/text()[2]')
                movieTime = movie.xpath('./a/div/div[4]/text()[2]')
                item['movieTitle'] = movieTitle.extract_first()
                item['movieType'] = movieType.extract_first()
                item['movieTime'] = movieTime.extract_first()
                yield item
        except Exception as e:
            print(e)
        finally:
            pass
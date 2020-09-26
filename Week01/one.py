#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
import pandas as pd
import requests
import lxml.etree
from bs4 import BeautifulSoup as bs


url = 'https://maoyan.com/films?showType=3'

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
          'Cookie': '_mta=209506861.1601122896662.1601123399567.1601123417756.11; uuid=404c7c8b6547442eb18e.1601122879.1.0.0; mtcdn=K; userTicket=UuswDWChlvGxavTfgEKcHYixOzXSLQXZpHYonOgI; n=RYY296572655; lsu=; SERV=maoyan; LREF=aHR0cHM6Ly9tYW95YW4uY29tL3Bhc3Nwb3J0L2xvZ2luP3JlZGlyZWN0PSUyRmZpbG1zJTNGc2hvd1R5cGUlM0Qz; passport.sid=jcsli5vtlLgxLf-E-YF1PkppAA54v_9j; passport.sid.sig=prgqNixkqLuTh-C72W926I9vlQU'}
response = requests.get(url, headers=header)


bs_info = bs(response.text, 'html.parser')
url_base = 'https://maoyan.com'
urls = []


for tags in bs_info.find_all('div', attrs={'class': 'channel-detail'}):
    for atag in tags.find_all('a'):
        url_back = atag.get('href')
        url_full = url_base + url_back
        urls.append(url_full)

my_list = []
for i in urls[0:10]:
    time.sleep(1)
    total_response = requests.get(i, headers=header)
    selector = lxml.etree.HTML(total_response.text)
    film_name = selector.xpath('//*[@id="app"]/div/div[1]/div/div[1]/span/text()')
    film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a/text()')
    show_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
    my_list.append((film_name, film_type, show_date))


films = pd.DataFrame(data=my_list)
films.to_csv('./mm44466.csv', encoding='utf-8', index=False, header=False)
print("Sucessful")

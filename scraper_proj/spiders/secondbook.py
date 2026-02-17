# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:10:36 2021

@author: acer
"""

import scrapy
from scraper_proj.items import ScraperProjItem

class SecondSpider(scrapy.Spider):
    name="Books2"
    start_urls = [
            "http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html",
        ]
    
    def parse(self, response):
        item = ScraperProjItem()
        #item['title'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1').extract()
        #item['price'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]').extract()
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()
        
        return item
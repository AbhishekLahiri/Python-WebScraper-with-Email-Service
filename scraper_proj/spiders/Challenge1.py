# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 21:16:08 2021

@author: acer
"""

import scrapy
from scraper_proj.items import ScraperProjItem

class SpiderChallenge1(scrapy.Spider):
    name="BookInfo"
    #allowed_domains[]
    start_urls = [
            "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
            "http://books.toscrape.com/catalogue/the-requiem-red_995/index.html",
            "http://books.toscrape.com/catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html",
            "http://books.toscrape.com/catalogue/olio_984/index.html"
        ]
    
    def parse(self, response):
        item = ScraperProjItem()
        item['title'] = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        item['category'] = response.xpath("//*[@id='default']/div/div/ul/li[3]/a/text()").get()
        item['price'] = response.xpath("//*[@id='content_inner']/article/div[1]/div[2]/p[1]/text()").get()
        item['in_stock'] = response.xpath("normalize-space(//*[@id='content_inner']/article/div[1]/div[2]/p[2])").get()
        
        return item
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 00:48:31 2021

@author: acer
"""

import requests
from bs4 import BeautifulSoup

r = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(r.content, 'lxml')

quotes = soup.find_all('div', class_='quote')
for x in quotes:
    print(x.find('span').text)
    
tags = soup.find_all('div', class_='tags')
for t in tags:
    print(t.text)
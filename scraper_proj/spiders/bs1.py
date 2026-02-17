# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 00:08:57 2021

@author: acer
"""

import requests
from bs4 import BeautifulSoup

r = requests.get('https://google.com')
# print(r.status_code)  #check HTTP response status codes to find the issue
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)

soup = BeautifulSoup(r.content, 'lxml')

print(soup.prettify())
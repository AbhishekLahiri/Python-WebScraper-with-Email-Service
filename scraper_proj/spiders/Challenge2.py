# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:11:41 2021

@author: acer
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time #not mandatory

def review_count_scrap():
    url = 'https://www.amazon.in/gp/bestsellers'
    headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    print(r.status_code)
    
    # product_total_review = soup.find_all('a', class_='a-size-small a-link-normal')
    # for pd in product_total_review:
    #     print(pd.text)
    
    product_total_review = [i.text for i in soup.findAll('a', {'class': 'a-size-small a-link-normal'})]
    data_frame = pd.DataFrame(product_total_review)
    print(data_frame)
    
    #add timer
    time.sleep(60)
    
end_timer = time.time() + 60*2
while time.time() < end_timer:
    review_count_scrap()

    
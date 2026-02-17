# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:18:08 2021

@author: acer
"""

import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data(url):
    url = url
    headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    course_info = [i.text for i in soup.findAll('span', {'class': 'desc'})]
    data_frame = pd.DataFrame(course_info)
    opp_text = [i.find('p').text for i in soup.findAll('div', {'class': 'single-path-article-content'})]
    data_frame2 = pd.DataFrame(opp_text)
    instructor = [i.text for i in soup.findAll('p', {'class': 'name'})]
    data_frame3 = pd.DataFrame(instructor)
    print(data_frame)
    print(data_frame2)
    print(data_frame3)

driver = webdriver.Chrome()
driver.get("https://sdsclub.com/")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="menu-item-456"]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="category-career"]/div/div[2]/div[4]/div/figure/a').click()
time.sleep(10)
parent = driver.current_window_handle
others = driver.window_handles
for w in others:
    if w!=parent:
        driver.switch_to.window(w)
        driver.close()
    time.sleep(0.5)
time.sleep(2)


get_data(driver.current_url)



time.sleep(5)
driver.quit()


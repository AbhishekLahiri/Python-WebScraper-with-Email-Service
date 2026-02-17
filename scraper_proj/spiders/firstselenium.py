# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:52:47 2021

@author: acer
"""

import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.amazon.in");
time.sleep(5)

driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').click()

# #for entering user credentials
# def site_login():
#     driver.find_element_by_id('username').send_keys('uname')
#     driver.find_element_by_id('password').send_keys('pwd')




time.sleep(5)

driver.quit()

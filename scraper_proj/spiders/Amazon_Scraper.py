# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 23:46:31 2021

@author: acer
"""

import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tabulate import tabulate

driver = webdriver.Chrome()
driver.get("https://www.amazon.in");
time.sleep(5)

driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').click()
driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys('bluetooth headphones')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="p_72/1318476031"]/span/a/section').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="n/14146390031"]/span/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="p_36/1318504031"]/span/a').click()
time.sleep(3)

products = []
url = driver.current_url
headers = ({'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')

while True:    
    links = soup.find_all('a', {'class': 'a-link-normal a-text-normal'})
    for i in links:
        products.append('https://www.amazon.in' + i.get('href'))
    try:
        nextpg = driver.find_element_by_partial_link_text('Next')
        if nextpg.is_enabled():
            nextpg.click()
            time.sleep(5)
        else:
            break
    except Exception:
        break


print(len(products))
df = pd.DataFrame(products, columns=['Links'])

time.sleep(5)
driver.quit()

col_list = list(df.columns.values)
data = df
text = """
Hello..

Choose one:

{table}

Regards,

Your Friendly Crawler"""

html = """
<html>
<head>
<style> 
 table, th, td {{ border: 1px solid black; border-collapse: collapse; }}
  th, td {{ padding: 5px; }}
</style>
</head>
<body><p>Get your bluetooth headphone!!</p>
<p>From 4-star reviewed products below:</p>
{table}
<p>Regards,</p>
<p>Your Friendly Crawler</p>
</body></html>
"""
text = text.format(table=tabulate(data, headers=col_list, tablefmt="grid"))
html = html.format(table=tabulate(data, headers=col_list, tablefmt="html"))
mail = MIMEMultipart("alternative", None, [MIMEText(text), MIMEText(html,'html')])

mail['Subject'] = 'Best Budget Headphone!'
mail['From'] = 'crawledforyou@gmail.com'
mail['To'] = 'agnish1497@gmail.com'

#allow browser login for email
conn = smtplib.SMTP('smtp.gmail.com', 587)
#USE SSL RECOMMENDED
conn.starttls()
conn.login('crawledforyou@gmail.com', 'password')
conn.sendmail('crawledforyou@gmail.com', 'agnish1497@gmail.com', mail.as_string())
conn.quit()

print('\nScraped data sent successfully!!')

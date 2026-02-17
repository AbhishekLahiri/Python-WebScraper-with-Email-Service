# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:58:12 2021

@author: acer
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import time

while True:
    url = 'https://pastebin.com/Mfc9txQV'
    headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    
    if str(soup).find('Key') == -1:
        time.sleep(300)
        continue
    else:
        print('ALERT!!!')
        
        #email
        email_subject = 'ALERT!!! Check site. Sensitive information noticed!'
        from_email = 'crawledforyou@gmail.com'
        to_email = 'neha.ray1999@gmail.com'
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        #USE SSL RECOMMENDED
        conn.starttls()
        conn.login('crawledforyou@gmail.com', 'password')
        conn.sendmail(from_email, to_email, email_subject)
        conn.close()
        
        print('Alert sent...')
        
        break
    

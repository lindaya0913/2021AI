#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from random import uniform

URL="https://tw.appledaily.com/life/20210815/HJSJV6YOAZA27KBUVQ674C7WRU/"

PATH = "D10\chromedriver_win32\chromedriver.exe"
Chrome_driver = webdriver.Chrome(PATH)
Chrome_driver.get(URL)
html = Chrome_driver.page_source

time.sleep(uniform(0.8,1)*5)

Chrome_driver.quit()

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
title = soup.find('div',{'class':'article__header'})
textlist = soup.find_all('p',{'class': 'text--desktop'})
text = ''
for part_text in textlist: 
	text += part_text.text
print(text)

file = open("news.txt", "w+",encoding='utf-8')
file.write(text)
file.close()
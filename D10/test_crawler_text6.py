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

soup = BeautifulSoup(html, 'lxml')
title= soup.find('div',{'class':'article__header'})

Title_text1= title.find('span')
Title_text2= title.div.h1.span
print(Title_text1)
print(Title_text2)




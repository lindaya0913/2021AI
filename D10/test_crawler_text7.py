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

# Chrome_driver.quit()

# from bs4 import BeautifulSoup

# soup = BeautifulSoup(html, 'lxml')
# textlist = soup.find_all('p',{'class': 'text--desktop text--mobile article-text-size_md  tw-max_width'})
# # text=''
# # for part_text in textlist: 
# # 	text=text+part_text.text
# print(textlist)





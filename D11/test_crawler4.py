from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from random import uniform
import os

apple_url = "https://tw.appledaily.com/home/"

PATH = "D10\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(apple_url)


time.sleep(uniform(0.8,1)*5)
driver.maximize_window()
input = driver.find_element_by_xpath('//*[@id="global-header"]/header/div/div[2]/form/input')
input.send_keys("蘇")
input.send_keys(Keys.RETURN)

time.sleep(uniform(0.8,1)*5)
# for i in range(3):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(uniform(0.8,1)*5)


main_container = driver.find_element_by_class_name("article-container")
main_container = main_container.get_attribute("innerHTML")

driver.quit()

from bs4 import BeautifulSoup

soup = BeautifulSoup(main_container, "html.parser")
print(soup.prettify())
news = soup.find_all('a',{'class':'story-card'})
news_href = []
for new in news:
    news_href.append(apple_url + new['href'])

print(news_href[0])
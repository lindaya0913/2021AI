from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


PATH = "D10\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://tw.appledaily.com/home/")


time.sleep(5)
driver.maximize_window()
input = driver.find_element_by_xpath('//*[@id="global-header"]/header/div/div[2]/form/input')
input.send_keys("五倍")
input.send_keys(Keys.RETURN)


time.sleep(5)

docs = driver.find_elements_by_class_name("story-card")
for doc in docs:
    print(doc.get_attribute("href"))

driver.quit()
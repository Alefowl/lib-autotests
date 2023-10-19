import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8080/123/add-mb/')
time.sleep(3)
title = driver.find_element("xpath", "//input[@id='title']")
title.send_keys("Береза")
author = driver.find_element("xpath", "//select//option[@value='3']").click()
chapters = driver.find_element("xpath", "//div//input[@id='size']")
chapters.send_keys("5")
language = driver.find_element("xpath", "//select//option[@value='2']")
language.click()
date = driver.find_element("xpath", "//div//input[@id='create_date']")
date.send_keys('1920')
add = driver.find_element("xpath", "//input[@value='Add metabook']")
time.sleep(5)
add.click()

time.sleep(5)
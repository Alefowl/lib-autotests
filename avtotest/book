import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://127.0.0.1:8080/123/add-b/')
time.sleep(3)
title = driver.find_element("xpath", '//input[@id="title"]')
title.send_keys("Март")
title = driver.find_element("xpath", '//input[@id="author"]')
title.send_keys("Тютчев")
metabook = driver.find_element("xpath", '//select//option[@value="1"]')
metabook.click()
year = driver.find_element("xpath", '//input[@id="translation_date"]')
year.send_keys('1926')
language = driver.find_element("xpath", '//option[@value="1"]')
language.click()
btn = driver.find_element("xpath", '//input[@value="Add book"]')
btn.click()
time.sleep(4)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://127.0.0.1:8080/123/add-t/')
time.sleep(3)
book = driver.find_element("xpath", '//option[@value="24"]')
text = driver.find_element("xpath", '//textarea[@id="title"]')
text.send_keys("{ 1 | dssssss { ")
bnt = driver.find_element("xpath", '//input[@value="Add text"]')
bnt.click()
time.sleep(5)
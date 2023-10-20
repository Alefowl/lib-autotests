import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://127.0.0.1:8080/auth/authentication')
time.sleep(3)

name = driver.find_element("xpath", '//input[@name="login"]')
name.send_keys("123")
password = driver.find_element("xpath", '//input[@name="password"]')
password.send_keys("123456")
btn = driver.find_element("xpath", '//input[@value="Log in"]')
btn.click()
time.sleep(5)

tex = driver.find_element("xpath", '//tbody/tr[7]/td/a')
tex.click()
time.sleep(3)
book = driver.find_element("xpath", '//option[@value="24"]')
text = driver.find_element("xpath", '//textarea[@id="title"]')
text.send_keys("{ 1 | dssssss { ")
bnt = driver.find_element("xpath", '//input[@value="Add text"]')
bnt.click()
time.sleep(5)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8080/auth/registration')
name = driver.find_element("xpath", '//input[@name="login"]')
name.send_keys("123")
name2 = driver.find_element("xpath", '//input[@name="password"]')
name2.send_keys("123456")
loga = driver.find_element("xpath", '//input[@name="email"]')
loga.send_keys("fd@gmail.com")
btn = driver.find_element("xpath", '//input[@value="Register"]')
btn.click()
time.sleep(5)
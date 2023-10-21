import time
from selenium.webdriver.support import expected_conditions as EC, wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('http://127.0.0.1:8080/auth/authentication')
time.sleep(3)

name = driver.find_element("xpath", '//input[@name="login"]')
name.send_keys("123")
password = driver.find_element("xpath", '//input[@name="password"]')
password.send_keys("123456")
btn = driver.find_element("xpath", '//input[@value="Log in"]')
btn.click()
time.sleep(5)

bok = driver.find_element("xpath", '//tbody/tr[5]/td/a')
bok.click()
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

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert
time.sleep(3)
alert.accept()


alert = wait.until(EC.alert_is_present())

driver.switch_to.alert
time.sleep(3)
alert.accept()

time.sleep(3)
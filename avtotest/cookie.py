import os
import time
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
def cookie():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('http://127.0.0.1:8080/auth/authentication')
    time.sleep(3)

    name = driver.find_element("xpath", '//input[@name="login"]')
    name.send_keys("123")
    password = driver.find_element("xpath", '//input[@name="password"]')
    password.send_keys("123456")
    btn = driver.find_element("xpath", '//input[@value="Log in"]')
    btn.click()
    time.sleep(5)

    print(driver.get_cookies())


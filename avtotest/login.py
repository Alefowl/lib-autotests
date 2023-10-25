import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def login():
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8080/auth/authentication')
    name = driver.find_element("xpath", '//input[@name="login"]')
    name.send_keys("123")
    password = driver.find_element("xpath", '//input[@name="password"]')
    password.send_keys("123456")
    btn = driver.find_element("xpath", '//input[@value="Log in"]')
    btn.click()
    time.sleep(5)
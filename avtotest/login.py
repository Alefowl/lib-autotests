import time
from selenium import webdriver




def login(login1, password):
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8080/auth/authentication')
    name = driver.find_element("xpath", '//input[@name="login"]')
    name.send_keys(login1)
    password1 = driver.find_element("xpath", '//input[@name="password"]')
    password1.send_keys(password)
    btn = driver.find_element("xpath", '//input[@value="Log in"]')
    btn.click()
    time.sleep(5)
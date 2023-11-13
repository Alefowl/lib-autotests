import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service




def login(login1, password):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)


    driver.get('http://127.0.0.1:8080/auth/authentication')
    name = driver.find_element("xpath", '//input[@name="login"]')
    name.send_keys(login1)
    password1 = driver.find_element("xpath", '//input[@name="password"]')
    password1.send_keys(password)
    btn = driver.find_element("xpath", '//input[@value="Log in"]')
    btn.click()
    time.sleep(5)
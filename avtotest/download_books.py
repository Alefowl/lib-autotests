import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def download():
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

    mybooks = driver.find_element("xpath", '//tr[1]/td/a')
    mybooks.click()

    bulingual = driver.find_element("xpath", '//a[text()="bilingual"]')
    bulingual.click()
    btn = driver.find_element("xpath", '//p[2]/table/tbody/tr[1]/td[3]/button')
    btn.click()
    time.sleep(5)

    alert = wait.until(EC.alert_is_present())

    driver.switch_to.alert
    time.sleep(3)
    alert.accept()

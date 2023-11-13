import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def download(login, password):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10, poll_frequency=1)

    driver.get('http://127.0.0.1:8080/auth/authentication')
    time.sleep(3)

    name = driver.find_element("xpath", '//input[@name="login"]')
    name.send_keys(login)
    password1 = driver.find_element("xpath", '//input[@name="password"]')
    password1.send_keys(password)
    btn = driver.find_element("xpath", '//input[@value="Log in"]')
    btn.click()
    time.sleep(5)

    mybooks = driver.find_element("xpath", '/html/body/header/div/table/tbody/tr[3]/td/a')
    mybooks.click()
    time.sleep(3)
    bulingual = driver.find_element("xpath", '//a[text()="Шопен"]')
    bulingual.click()
    time.sleep(3)
    btn = driver.find_element("xpath", '//header/p[2]/table/tbody/tr[1]/td/button')
    btn.click()
    time.sleep(5)

    alert = wait.until(EC.alert_is_present())

    driver.switch_to.alert
    time.sleep(3)
    alert.accept()


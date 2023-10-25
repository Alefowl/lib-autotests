import time

import psycopg2
from selenium.webdriver.support import expected_conditions as EC, wait

from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

def add_metabook():
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

    metab = driver.find_element("xpath", '/html/body/header/div/table/tbody/tr[6]/td/a')
    metab.click()
    time.sleep(3)
    title = driver.find_element("xpath", "//input[@id='title']")
    title.send_keys("Береза")
    author = driver.find_element("xpath", "//select//option[@value='3']").click()
    chapters = driver.find_element("xpath", "//div//input[@id='size']")
    chapters.send_keys("5")
    language = driver.find_element("xpath", "//select//option[@value='2']")
    language.click()
    date = driver.find_element("xpath", "//div//input[@id='create_date']")
    date.send_keys('1920')
    add = driver.find_element("xpath", "//input[@value='Add metabook']")
    time.sleep(5)
    add.click()

    time.sleep(5)

    alert = wait.until(EC.alert_is_present())

    driver.switch_to.alert
    time.sleep(3)
    alert.accept()


    alert = wait.until(EC.alert_is_present())

    driver.switch_to.alert
    time.sleep(3)
    alert.accept()

    time.sleep(3)

    connect = psycopg2.connect(host='localhost', user='postgres', password='10121991', dbname='kapinuss')
    cursor = connect.cursor()
    cursor.execute("SELECT title FROM metabooks WHERE title = 'Береза'")
    row = cursor.fetchone()

    if row and row[0] == 'Береза':
        print("Метабук найден")
    else:
        print("Метабук не найдена.")

    cursor.close()
    connect.close()
import time

import psycopg2
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def add_book(login, password, title, author, date, metabooks):
    driver = webdriver.Chrome()
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

    bok = driver.find_element("xpath", '//tbody/tr[5]/td/a')
    bok.click()
    time.sleep(3)
    title1 = driver.find_element("xpath", '//input[@id="title"]')
    title1.send_keys(title)
    title2 = driver.find_element("xpath", '//input[@id="author"]')
    title2.send_keys(author)

    year = driver.find_element("xpath", '//input[@id="translation_date"]')
    year.send_keys(date)
    language = driver.find_element("xpath", '//option[@value="1"]')
    language.click()
    metabooks1 = ("xpath", '//select[@id="metabook"]')
    metabook = Select(driver.find_element(*metabooks1))
    metabook.select_by_visible_text(metabooks)
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

    connect = psycopg2.connect(host='localhost', user='postgres', password='10121991', dbname='kapinuss')
    cursor = connect.cursor()
    cursor.execute("SELECT title FROM books WHERE title = 'Вий'")
    row = cursor.fetchone()

    if row and row[0] == 'Вий':
        print("Книга найдена")
    else:
        print("Книга не найдена.")

    cursor.close()
    connect.close()


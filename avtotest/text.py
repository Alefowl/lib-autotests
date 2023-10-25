import time

import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def add_text():
    driver = webdriver.Chrome()

    driver.get('http://127.0.0.1:8080/auth/authentication')
    time.sleep(3)

    name = driver.find_element("xpath", '//input[@name="login"]')
    name.send_keys("123")
    password = driver.find_element("xpath", '//input[@name="password"]')
    password.send_keys("123456")
    btn = driver.find_element("xpath", '//input[@value="Log in"]')
    btn.click()
    time.sleep(5)

    tex = driver.find_element("xpath", '//tbody/tr[7]/td/a')
    tex.click()
    time.sleep(3)
    book1 = ("xpath", '//select[@id="book"]')
    dorop = Select(driver.find_element(*book1))
    dorop.select_by_visible_text("Март1")
    text = driver.find_element("xpath", '//textarea[@id="title"]')
    text.send_keys("{ 1 | dssssss { ")
    bnt = driver.find_element("xpath", '//input[@value="Add text"]')
    bnt.click()
    time.sleep(5)

    connect = psycopg2.connect(host='localhost', user='postgres', password='10121991', dbname='kapinuss')
    cursor = connect.cursor()
    cursor.execute("SELECT txt FROM uploads WHERE txt = '{ 1 | dssssss {'")
    row = cursor.fetchone()

    if row and row[0] == '{ 1 | dssssss { ':
        print("Текст добавлен")
    else:
        print("Текст не добавлен")

    cursor.close()
    connect.close()


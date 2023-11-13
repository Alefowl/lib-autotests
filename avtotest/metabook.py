import time

import psycopg2
from selenium.webdriver.support import expected_conditions as EC, wait
>>>>>>> master
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def add_metabook(login, password, title, size, create_date, authors):
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
    metab = driver.find_element("xpath", '//tbody/tr[6]/td/a')
    metab.click()
    time.sleep(3)
    title1 = driver.find_element("xpath", "//input[@id='title']")
    title1.send_keys(title)

    chapters = driver.find_element("xpath", "//div//input[@id='size']")
    chapters.send_keys(size)
    language = driver.find_element("xpath", "//select//option[@value='2']")
    language.click()
    date = driver.find_element("xpath", "//div//input[@id='create_date']")
    date.send_keys(create_date)
    author = ("xpath", '//select[@id="author"]')
    author1 = Select(driver.find_element(*author))
    author1.select_by_visible_text(authors)
    time.sleep(3)
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
    cursor.execute("SELECT title FROM metabooks WHERE title = 'Вий'")
    row = cursor.fetchone()

    if row and row[0] == 'Вий':
        print("Метабук найден")
    else:
        print("Метабук не найден.")

    cursor.close()
    connect.close()


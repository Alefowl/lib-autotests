import time
import psycopg2
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def add_text(login, password, name_book):
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
    driver.execute_script("window.scrollBy(0, 500);")
    tex = driver.find_element("xpath", '//tbody/tr[7]/td/a')
    tex.click()
    time.sleep(3)
    book1 = ("xpath", '//select[@id="book"]')
    dorop = Select(driver.find_element(*book1))
    dorop.select_by_visible_text(name_book)
    text = driver.find_element("xpath", '//textarea[@id="title"]')
    text.send_keys("{ 1 | dssssss { ")
    page_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Прокрутка до конца страницы
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_page_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(2)
        if new_page_height == page_height:
            break
        # Обновление высоты страницы
        page_height = new_page_height
    bnt = driver.find_element("xpath", '//input[@value="Add text"]')
    bnt.click()
    time.sleep(5)

    connect = psycopg2.connect(host='localhost', user='postgres', password='10121991', dbname='kapinuss')
    cursor = connect.cursor()
    cursor.execute("SELECT txt FROM uploads WHERE txt = '{ 1 | dssssss { '")
    row = cursor.fetchone()

    if row and row[0] == '{ 1 | dssssss { ':
        print("Текст добавлен")
    else:
        print("Текст не добавлен")

    cursor.close()
    connect.close()
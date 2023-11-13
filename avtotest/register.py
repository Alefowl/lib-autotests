import time
import psycopg2
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def register(login, password, email):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('http://127.0.0.1:8080/auth/registration/')
    name = driver.find_element("xpath", '//input[@name="login"]')
    name.send_keys(login)
    name2 = driver.find_element("xpath", '//input[@name="password"]')
    name2.send_keys(password)
    loga = driver.find_element("xpath", '//input[@name="email"]')
    loga.send_keys(email)
    btn = driver.find_element("xpath", '//input[@value="Register"]')
    btn.click()
    time.sleep(5)

    connect = psycopg2.connect(host='localhost', user='postgres', password='10121991', dbname='kapinuss')
    cursor = connect.cursor()
    cursor.execute("SELECT login FROM users WHERE login = '123' ")
    row = cursor.fetchone()

    if row and row[0] == '123':
        print("Запись авторизации найдена!")
    else:
        print("Запись авторизации не найдена.")
    cursor.close()
    connect.close()


import time
import psycopg2
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def register_and_check_user():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Переходим в браузере по адресу
    driver.get('http://localhost:81/auth/registration')
    time.sleep(1)

    #  Проверка URL страницы
    url = driver.current_url
    print("Страница регистрации", url, "OK")
    assert url == "http://localhost:81/auth/registration", "Url другой страницы"

    # Вводим значение в поле логин
    login = driver.find_element("xpath", '//input[@name="login"]')
    login.send_keys("test")

    #  Вводим значение в поле пароль
    password = driver.find_element("xpath", '//input[@name="password"]')
    password.send_keys("test1")

    #  Вводим значение в поле email
    email = driver.find_element("xpath", '//input[@name="email"]')
    email.send_keys("test@gmail.com")

    #  Нажимаем на кнопку регистрации
    btn = driver.find_element("xpath", '//input[@value="Register"]')
    btn.click()
    time.sleep(1)

    #  Перенаправляемся на страницу авторизации
    url = driver.current_url
    print("Переход на страницу авторизации", url, "OK")
    assert url == "http://localhost:81/auth/authentication", "Url другой страницы"

    #  Подключаемся к БД
    connect = psycopg2.connect(host='localhost', user='postgres', password='12345', dbname='kapinuss')
    cursor = connect.cursor()
    cursor.execute("SELECT login FROM users WHERE login = 'test' ")
    row = cursor.fetchone()
    if row and row[0] == 'test':
        print("Запись", row, "найдена в БД!")
    else:
        print("Запись", row, "не найдена в БД!")
    cursor.close()
    connect.close()


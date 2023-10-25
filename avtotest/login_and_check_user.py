import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def login_and_check_user():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Переход на страницу авторизации
    driver.get('http://localhost:81/auth/authentication')
    time.sleep(5)

    #  Проверка URL страницы
    url = driver.current_url
    print("Страница аторизации", url, "OK")
    assert url == "http://localhost:81/auth/authentication", "Url другой страницы"


    login = driver.find_element("xpath", '//input[@name="login"]')
    login.send_keys("test")

    password = driver.find_element("xpath", '//input[@name="password"]')
    password.send_keys("test1")

    btn = driver.find_element("xpath", '//input[@value="Log in"]')
    btn.click()
    time.sleep(5)

    # Переход на страницу личного кабинета
    url = driver.current_url
    print("Переход на страницу личного кабинета:", url)

    expected_url = "http://localhost:81/test/private"
    assert url.startswith(expected_url), "URL другой страницы"




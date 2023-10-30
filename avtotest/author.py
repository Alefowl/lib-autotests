import time
import psycopg2
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait





def add_author(login1, password, english_name, russian_name, german_name, french_name, birth_date, death_date):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    driver.get('http://127.0.0.1:8080/auth/authentication')
    time.sleep(3)

    name = driver.find_element("xpath", '//input[@name="login"]')
    name.send_keys(login1)
    password1 = driver.find_element("xpath", '//input[@name="password"]')
    password1.send_keys(password)
    btn = driver.find_element("xpath", '//input[@value="Log in"]')
    btn.click()
    time.sleep(5)

    author = driver.find_element("xpath", '/html/body/header/div/table/tbody/tr[4]/td/a')
    author.click()
    time.sleep(3)
    english = driver.find_element(By.XPATH, '//input[@id="english_name"]')
    english.send_keys(english_name)
    rus = driver.find_element(By.XPATH, '//input[@id="russian_name"]')
    rus.send_keys(russian_name)
    german = driver.find_element(By.XPATH, '//input[@id="german_name"]')
    german.send_keys(german_name)
    french = driver.find_element(By.XPATH, '//input[@id="french_name"]')
    french.send_keys(french_name)
    birth = driver.find_element(By.XPATH, '//input[@id="birth_date"]')
    birth.send_keys(birth_date)
    death = driver.find_element(By.XPATH, '//input[@id="death_date"]')
    death.send_keys(death_date)
    languages = driver.find_element(By.XPATH, '//select[@id="language"]/option[@value="2"]')
    languages.click()
    time.sleep(3)
    add_book = driver.find_element(By.XPATH, '//input[@type="submit"]')
    add_book.click()
    time.sleep(3)

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
    cursor.execute("SELECT russian_name FROM creators WHERE russian_name = 'Гоголь'")
    row = cursor.fetchone()

    if row and row[0] == 'Гоголь':
        print("Автор найден")
    else:
        print("Автор не найдена.")

    cursor.close()
    connect.close()
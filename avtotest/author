import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get('http://127.0.0.1:8080/123/add-a/')
time.sleep(3)
english = driver.find_element(By.XPATH, '//input[@id="english_name" and @required=""]')
english.send_keys('Dostoevskii')
rus = driver.find_element(By.XPATH, '//input[@id="russian_name"]')
rus.send_keys('Достоевский')
german = driver.find_element(By.XPATH, '//input[@id="german_name"]')
german.send_keys('Dostoevskii')
french = driver.find_element(By.XPATH, '//input[@id="french_name"]')
french.send_keys('Dostoevskii')
birth = driver.find_element(By.XPATH, '//input[@id="birth_date"]')
birth.send_keys('1903')
death = driver.find_element(By.XPATH, '//input[@id="death_date"]')
death.send_keys('1920')
languages = driver.find_element(By.XPATH, '//select[@id="language"]/option[@value="2"]')
languages.click()
time.sleep(3)
add_book = driver.find_element(By.XPATH, '//input[@type="submit"]')
add_book.click()
time.sleep(10)

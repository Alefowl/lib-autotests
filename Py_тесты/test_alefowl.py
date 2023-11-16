import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from login_pages import USERNAME_FIELD, PASSWORD_FIELD, SUBMIT_BUTTON

link = "http://127.0.0.1:8080/auth/authentication"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():


    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        name = browser.find_element(*USERNAME_FIELD)
        name.send_keys('gt1')
        password = browser.find_element(*PASSWORD_FIELD)
        password.send_keys('gt1')
        browser.find_element(*SUBMIT_BUTTON).click()





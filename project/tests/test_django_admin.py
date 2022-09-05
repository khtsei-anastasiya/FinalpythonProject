import pytest
import allure
from selenium import webdriver
import webdriver_manager.chrome
from project.pages.main_page import MainPageDjango


link = 'http://127.0.0.1:8000'


@pytest.fixture
def open_browser():
    with allure.step('Initializing chromedriver manager'):
        browser = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())
        browser.implicitly_wait(5)
        yield browser
    with allure.step('Closing browser'):
        browser.quit()


@allure.story('Open Django admin group page')
def open_django_admin(open_browser):
    main_page = MainPageDjango(open_browser, link)
    with allure.step('Open main page'):
        main_page.open_browser()
    with allure.step('Open Django admin'):
        main_page.open_admin_django()

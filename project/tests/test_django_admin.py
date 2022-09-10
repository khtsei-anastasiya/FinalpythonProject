import pytest
import allure
import urllib3
from selenium import webdriver
import webdriver_manager.chrome
from ..pages.main_page import MainPageDjango
from ..pages.django_admin_users import UsersPageDjango
from project.db_task import *

link = 'http://127.0.0.1:8000'


@pytest.fixture
def open_browser():
    with allure.step('Initializing chromedriver manager'):
        browser = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())
        browser.implicitly_wait(5)
        yield browser
    with allure.step('Closing browser'):
        browser.quit()


@allure.story('Check created group at the django admin')
def test_open_django_admin(open_browser):
    with allure.step('Insert group to db group'):
        group_adding()
    main_page = MainPageDjango(open_browser, link)
    with allure.step('Open main page'):
        main_page.open_browser()
    with allure.step('Open Django admin'):
        main_page.open_admin_django()
    with allure.step('Login'):
        main_page.login_user_django(username='admin', passwd='password')
    with allure.step('Open Group tab'):
        main_page.open_groups_tab()
    with allure.step('Verify group'):
        main_page.check_group_name(group='akhtsei')


@allure.story('Check user at DB added from UI')
def test_add_user_from_ui_at_db(open_browser):
    main_page = MainPageDjango(open_browser, link)
    with allure.step('Open main page'):
        main_page.open_browser()
    with allure.step('Open Django admin'):
        main_page.open_admin_django()
    with allure.step('Login'):
        main_page.login_user_django(username='admin', passwd='password')
    with allure.step('Open Users tab'):
        main_page.open_users_tab()
    with allure.step('Click Add user button'):
        users_page = UsersPageDjango(open_browser, link)
        users_page.open_add_users_page()
    with allure.step('Add User'):
        users_page.add_user(username='akhtsei', password='user12345', password2='user12345')
    with allure.step('Add user to the group'):
        users_page.add_user_to_group()
    with allure.step('Check username was added to the group'):
        user_belongs_to_group(username='akhtsei')



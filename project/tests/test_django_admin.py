import pytest
import allure
from selenium import webdriver
import webdriver_manager.chrome
from ..pages.main_page import MainPageDjango
from ..pages.django_admin_users import UsersPageDjango
from ..pages.django_admin_posts import PostsPageDjango
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


@allure.story('Check added from UI user belongs to the group via DB')
def test_check_via_db_user_added_from_ui_at_group(open_browser):
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


@allure.story('Newly created user can login to the admin')
def test_new_user_can_login_django_admin(open_browser):
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
        users_page.add_user(username='akhtsei2', password='user12345', password2='user12345')
        users_page.set_staff_status()
    with allure.step('Check user name at DB'):
        user_presents_at_users_table(username='akhtsei2')
    with allure.step('Log out admin'):
        main_page.user_log_out()
    with allure.step('Login new user'):
        main_page.login_again()
        main_page.login_new_user_django(username='akhtsei2', passwd='user12345')
        main_page.check_user_name(user_name='akhtsei2')


@allure.story('Img deletion verification')
def test_img_deleted_via_admin(open_browser):
    main_page = MainPageDjango(open_browser, link)
    with allure.step('Open main page'):
        main_page.open_browser()
    with allure.step('Check img source data'):
        main_page.get_img_attribute()
    with allure.step('Open Django admin'):
        main_page.open_admin_django()
    with allure.step('Login'):
        main_page.login_user_django(username='admin', passwd='password')
    with allure.step('Open posts page'):
        main_page.open_posts_tab()
        posts_page = PostsPageDjango(open_browser, link)
        posts_page.select_last_element()
        posts_page.delete_last_element()
    with allure.step('Click view site link'):
        main_page.view_site()
    with allure.step('Find deleted img'):
        main_page.check_img_deleted()


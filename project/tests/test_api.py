import allure
from ..pages.api_page import *


class TestApiCases:
    @allure.story('Work with the created user')
    def test_user_manipulations(self):
        with allure.step('Create user'):
            add_user_to_store(4, "test23", 'User', "ForTests2", "test123+12@gmail.com", "1234545", "+375291231249", 0)
        with allure.step('Login created user'):
            login_user("test23", "1234545")
        with allure.step('Get user data'):
            get_user_data("test23")
        with allure.step('Logout user'):
            logout_user()
        with allure.step('Delete user'):
            delete_user("1")
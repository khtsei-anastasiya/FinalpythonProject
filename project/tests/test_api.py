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
            delete_user("test23")

    @allure.story('Everything about your Pets')
    def test_pet_manipulations(self):
        with allure.step('Create new pet'):
            add_new_pet_to_store(pet_id=242424578, category_id=345, category_name='dog', pet_name='Welzevool',
                                 tags_id=234,
                                 tags_name='doggo', status="available")
        with allure.step('Check pet by id'):
            check_added_pet(pet_id=242424578)
        with allure.step('Update pet name'):
            update_pet_data(pet_id=242424578, category_id=345, category_name='dog', pet_name='Marley',
                            tags_id=234,
                            tags_name='doggo', status="available")
        with allure.step('Check updates'):
            check_pet_updates(pet_id=242424578, pet_name='Marley')

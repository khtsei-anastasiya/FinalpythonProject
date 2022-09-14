from project.locators.django_admin_users_page import UsersPageLocDjango
from project.pages.base_page import BasePage
from project.locators.main_page_loc import MainPageLoc
from project.locators.django_admin_main import MainPageLocDjango


class UsersPageDjango(BasePage):
    def open_add_users_page(self):
        find_add_btn = self.chrome.find_element(*UsersPageLocDjango.add_btn_loc)
        find_add_btn.click()

    def add_user(self, username: str, password: str, password2: str):
        find_user_field = self.chrome.find_element(*UsersPageLocDjango.username_field_loc)
        find_user_field.send_keys(username)
        find_pass_field = self.chrome.find_element(*UsersPageLocDjango.username_pass_loc)
        find_pass_field.send_keys(password)
        find_pass2_field = self.chrome.find_element(*UsersPageLocDjango.username_pass2_loc)
        find_pass2_field.send_keys(password2)
        find_safe_btn = self.chrome.find_element(*UsersPageLocDjango.save_btn_loc)
        find_safe_btn.click()

    def add_user_to_group(self):
        find_group = self.chrome.find_element(*UsersPageLocDjango.group_name_loc)
        find_group.click()
        find_add_btn = self.chrome.find_element(*UsersPageLocDjango.groups_add_btn)
        find_add_btn.click()
        find_safe_btn = self.chrome.find_element(*UsersPageLocDjango.save_btn_loc)
        find_safe_btn.click()

    def set_staff_status(self):
        find_status_control = self.chrome.find_element(*UsersPageLocDjango.staff_check_box)
        find_status_control.click()
        find_safe_btn = self.chrome.find_element(*UsersPageLocDjango.save_btn_loc)
        find_safe_btn.click()
from project.pages.base_page import BasePage
from project.locators.main_page_loc import MainPageLoc
from project.locators.django_admin_main import MainPageLocDjango
from project.pages.django_admin_users import UsersPageDjango
from project.locators.django_admin_users_page import UsersPageLocDjango

link = 'http://127.0.0.1:8000/admin/login/?next=/admin/'


class MainPageDjango(BasePage):
    def open_admin_django(self):
        find_admin_btn = self.chrome.find_element(*MainPageLoc.admin_btn)
        find_admin_btn.click()

    def login_user_django(self, username, passwd):
        find_username_field = self.chrome.find_element(*MainPageLoc.username_field)
        find_username_field.send_keys(username)
        find_passwd_field = self.chrome.find_element(*MainPageLoc.passwd_field)
        find_passwd_field.send_keys(passwd)
        find_login_btn = self.chrome.find_element(*MainPageLoc.login_btn)
        find_login_btn.click()

    def open_groups_tab(self):
        find_groups_link = self.chrome.find_element(*MainPageLocDjango.group_btn_loc)
        find_groups_link.click()

    def check_group_name(self, group: str):
        find_group_row = self.chrome.find_element(*MainPageLocDjango.group_row_loc).text
        assert find_group_row == group

    def open_users_tab(self):
        find_users_link = self.chrome.find_element(*MainPageLocDjango.user_btn_loc)
        find_users_link.click()

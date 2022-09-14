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

    def user_log_out(self):
        find_log_out_btn = self.chrome.find_element(*MainPageLocDjango.logout_btn)
        find_log_out_btn.click()

    def login_again(self):
        find_login_again_btn = self.chrome.find_element(*MainPageLocDjango.login_again_btn)
        find_login_again_btn.click()

    def login_new_user_django(self, username, passwd):
        find_username_field = self.chrome.find_element(*MainPageLoc.username_field)
        find_username_field.clear()
        find_username_field.send_keys(username)
        find_passwd_field = self.chrome.find_element(*MainPageLoc.passwd_field)
        find_passwd_field.clear()
        find_passwd_field.send_keys(passwd)
        find_login_btn = self.chrome.find_element(*MainPageLoc.login_btn)
        find_login_btn.click()

    def check_user_name(self, user_name: str):
        find_user_tools_row = self.chrome.find_element(*MainPageLocDjango.user_tools).text()
        print(find_user_tools_row)
        assert find_user_tools_row == user_name, f"Oops... User name {find_user_tools_row} does not match to {user_name}!"
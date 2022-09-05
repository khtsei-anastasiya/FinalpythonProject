from project.pages.base_page import BasePage
from project.locators.main_page_loc import MainPageLoc
from project.locators.django_admin_main import MainPageLocDjango

link = 'http://127.0.0.1:8000/admin/login/?next=/admin/'


class MainPageDjango(BasePage):
    def open_admin_django(self):
        find_admin_btn = self.chrome.find_element(MainPageLoc.admin_btn)
        find_admin_btn.click()

    def login_user_django(self, username, passwd):
        find_username_field = self.chrome.find_element(MainPageLoc.username_field)
        find_username_field.send_keys(username)
        find_passwd_field = self.chrome.find_element(MainPageLoc.passwd_field)
        find_passwd_field.send_keys(passwd)
        find_login_btn = self.chrome.find_element(MainPageLoc.login_btn)
        find_login_btn.click()

    def open_groups_tab(self):
        find_groups_link = self.chrome.find_element(MainPageDjango.group_btn_loc)
        find_groups_link.click()


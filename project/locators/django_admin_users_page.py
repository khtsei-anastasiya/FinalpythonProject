from selenium.webdriver.common.by import By


class UsersPageLocDjango:
    add_btn_loc = (By.XPATH, "//a[contains(text(),'Add user')]")
    username_field_loc = (By.XPATH, "//input[@id='id_username']")
    username_pass_loc = (By.XPATH, "//input[@id='id_password1']")
    username_pass2_loc = (By.XPATH, "//input[@id='id_password2']")
    save_btn_loc = (By.XPATH, "//input[@name='_save']")
    add_another_btn_loc = (By.XPATH, "//input[@name='_addanother']")
    continue_btn_loc = (By.XPATH, "//input[@name='_continue']")


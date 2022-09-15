from selenium.webdriver.common.by import By


class MainPageLocDjango:
    main_page_url_loc = 'http://127.0.0.1:8000/admin/auth/'
    group_page_url_loc = 'http://127.0.0.1:8000/admin/auth/group/'

    group_btn_loc = (By.XPATH, '//a[contains(text(),"Groups")]')
    group_row_loc = (By.XPATH, '//th[@class="field-__str__"]')
    user_btn_loc = (By.XPATH, '//a[contains(text(),"Users")]')
    logout_btn = (By.XPATH, '//button[contains(text(),"Log out")]')
    login_again_btn = (By.XPATH, "//a[contains(text(),'Log in again')]")
    user_tools = (By.XPATH, '//div[@id="user-tools"]/strong')
    posts_button_loc = (By.XPATH, '//a[contains(text(),"Posts")]')
    view_page_link = (By.XPATH, '//a[contains(text(),"View site")]')




from selenium.webdriver.common.by import By


class MainPageLocDjango:
    main_page_url_loc = 'http://127.0.0.1:8000/admin/auth/'
    group_page_url_loc = 'http://127.0.0.1:8000/admin/auth/group/'

    group_btn_loc = (By.XPATH, '//a[contains(text(),"Groups")]')
    group_row_loc = (By.XPATH, '//th[@class="field-__str__"]')
    user_btn_loc = (By.XPATH, '//a[contains(text(),"Users")]')

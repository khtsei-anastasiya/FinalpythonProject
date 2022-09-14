from selenium.webdriver.common.by import By


class MainPageLoc:
    main_page_url_loc = 'http://127.0.0.1:8000'
    admin_btn = (By.XPATH, '//a[contains(text(),"Go to Admin")]')
    username_field = (By.XPATH, '//input[@id="id_username"]')
    passwd_field = (By.XPATH, '//input[@id="id_password"]')
    login_btn = (By.XPATH, '//input[@type="submit"]')


from selenium.webdriver.common.by import By


class PostsPageLoc:
    last_elem_at_table = (By.XPATH, "(//table[@id='result_list']//input[@class='action-select'])[last()]")
    drop_down = (By.XPATH, "//select[@name='action']")
    delete_value_drop_down = (By.XPATH, "//select[@name='action']//option[@value='delete_selected']")
    go_btn = (By.XPATH, "//button[contains(text(),'Go')]")
    submit_btn = (By.XPATH, "//input[@type='submit']")


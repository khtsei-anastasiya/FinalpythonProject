from project.pages.base_page import BasePage
from project.locators.gjango_admin_posts_page import PostsPageLoc


class PostsPageDjango(BasePage):
    def select_last_element(self):
        last_row = self.chrome.find_element(*PostsPageLoc.last_elem_at_table)
        last_row.click()
        select_drop_down = self.chrome.find_element(*PostsPageLoc.drop_down)
        select_drop_down.click()
        select_value_drop_down = self.chrome.find_element(*PostsPageLoc.delete_value_drop_down)
        select_value_drop_down.click()
        tap_go = self.chrome.find_element(*PostsPageLoc.go_btn)
        tap_go.click()

    def delete_last_element(self):
        confirm_deletion = self.chrome.find_element(*PostsPageLoc.submit_btn)
        confirm_deletion.click()

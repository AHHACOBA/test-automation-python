from selenium.webdriver.common.by import By
from pages.base_page import Page


class MenuPage(Page):
    AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
    AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")

    def click_music_menu(self):
        self.click(*self.AMAZON_MUSIC_MENU_ITEM)

    def verify_items_amount(self, expected_item_count):
        actual_item_count = len(self.driver.find_elements(*self.AMAZON_MUSIC_MENU_ITEM_RESULTS))
        assert expected_item_count == str(actual_item_count), f'Expected text {expected_item_count}, but got {actual_item_count}'

from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    HAM_MENU = (By.ID, 'nav-hamburger-menu')
    ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
    SEARCH_CART = (By.ID, 'nav-cart')

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS_LINK)

    def click_cart(self):
        self.click(*self.SEARCH_CART)

    def click_ham_menu(self):
        self.click(*self.HAM_MENU)


from pages.base_page import Page
from selenium.webdriver.common.by import By

class Cart(Page):
    CART_HEADER = (By.CSS_SELECTOR, "h1.sc-empty-cart-header")

    def verify_cart(self, cart_message):
        self.verify_text(cart_message, *self.CART_HEADER)
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Product(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    SIZE_SELECTION_TOOLTIP = (By.ID, 'a-popover-content-1')
    LINK_TO_HOVER = (By.CSS_SELECTOR, 'div#nav-subnav a[href*=sales]')
    FLYOUT_MENU_OPTION = (By.CSS_SELECTOR, 'div.mega-menu img[src*=flyout]')

    def open_product(self, productid):
        # https://www.amazon.com/gp/product/B074TBCSC8
        self.open_page(f'gp/product/{productid}')

    def hover_add_to_cart(self):
        cart_button = self.find_element(*self.ADD_TO_CART_BTN)
        self.actions.move_to_element(cart_button).perform()
        #sleep(5)

    def hover_over_link(self):
        link_to_hover = self.find_element(*self.LINK_TO_HOVER)
        self.actions.move_to_element(link_to_hover).perform()

    def verify_size_tooltip(self):
        self.wait_for_element_appear(*self.SIZE_SELECTION_TOOLTIP)

    def verify_flyout_shown(self):
        self.wait_for_element_appear(*self.FLYOUT_MENU_OPTION)


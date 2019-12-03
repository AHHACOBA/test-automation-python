from pages.main_page import MainPage
from pages.search_results_page import SearchResults
from pages.signin_page import SignInPage
from pages.cart_page import Cart
from pages.menu_page import MenuPage
from pages.product_page import Product

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.signin_page = SignInPage(self.driver)
        self.cart_page = Cart(self.driver)
        self.menu_page = MenuPage(self.driver)
        self.product_page = Product(self.driver)



from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    signin_url = 'https://www.amazon.com/ap/signin'

    def verify_signin_page(self):
        assert self.signin_url in self.driver.current_url, f'Expected url {self.signin_url}, but got {self.driver.current_url}'

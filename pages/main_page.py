from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.select import Select


class MainPage(Page):
    HAM_MENU = (By.ID, 'nav-hamburger-menu')
    ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
    SEARCH_CART = (By.ID, 'nav-cart')
    SELECT_DEPARTMENT = (By.ID, 'searchDropdownBox')
    SELECTED_DEPARTMENT_SPAN = (By.CSS_SELECTOR, '#nav-search-dropdown-card span.nav-search-label')
    #'div.mega-menu a ul.mm-category-list')[0]

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS_LINK)

    def click_cart(self):
        self.click(*self.SEARCH_CART)

    def click_ham_menu(self):
        self.click(*self.HAM_MENU)

    def select_department(self, department):
        select_department_element = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(select_department_element)
        #select.select_by_value("search-alias=stripbooks")
        select.select_by_visible_text(department)


    def verify_selected_department(self, expected_department):
        self.verify_text(expected_department, *self.SELECTED_DEPARTMENT_SPAN)





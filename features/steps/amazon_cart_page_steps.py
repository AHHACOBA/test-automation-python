from behave import then
from selenium.webdriver.common.by import By

CART_HEADER = (By.CSS_SELECTOR, "h1.sc-empty-cart-header")


@then('Verify that Shopping Cart is empty')
def verify_cart(context):
    cart_empty = context.driver.find_element(*CART_HEADER).text
    assert cart_empty in context.driver.page_source






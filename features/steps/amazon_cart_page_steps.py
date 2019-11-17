from behave import then
from selenium.webdriver.common.by import By
from time import sleep

CART_HEADER = (By.CSS_SELECTOR, "h1.sc-empty-cart-header")
CART_ITEM = (By.CSS_SELECTOR, "span.a-list-item a.sc-product-link[href*='B00NLR1PX0']")

@then('Verify text is {cart_message}')
def verify_cart(context, cart_message):
    #cart_empty_text = context.driver.find_element(*CART_HEADER).text
      #assert cart_empty_text in context.driver.page_source
    #assert cart_message in cart_empty_text
    context.app.cart_page.verify_cart(cart_message)


@then('Verify that cart has {expected_item} item')
def verify_cart_item(context, expected_item):
    sleep(3)
    actual_item_text = context.driver.find_element(*CART_ITEM).text
    assert expected_item in actual_item_text
    #assert actual_item_text.find(expected_item) > -1, f'Expected text is {expected_item}, but got {actual_item_text}'





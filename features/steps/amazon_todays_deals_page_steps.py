from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

TODAYS_DEALS_HEADER = (By.CSS_SELECTOR, 'div.a-row.a-spacing-top-small.suppleTitle h1')
RANDOM_PRODUCT = (By.XPATH, "//a[contains(text(), 'See details')]")
DEAL_PRODUCT = (By.CSS_SELECTOR, "a.a-link-normal img")
BTN_CLICK = (By.ID, 'add-to-cart-button')
CLOSE_POPUP = (By.ID, 'attach-close_sideSheet-link')

@then('{expected_header} are showing')
def header_is_correct(context, expected_header):
    actual_header = context.driver.find_element(*TODAYS_DEALS_HEADER).text
    assert actual_header == expected_header, f'Expected {expected_header}, but got {actual_header}'


@then('Click on any product to add it to the cart')
def click_any_product(context):
    context.driver.find_element(*RANDOM_PRODUCT).click()
    context.driver.wait.until(EC.element_to_be_clickable(DEAL_PRODUCT)).click()
    #context.driver.find_element(*DEAL_PRODUCT).click()
    context.driver.wait.until(EC.element_to_be_clickable(BTN_CLICK)).click()
    context.driver.wait.until(EC.element_to_be_clickable(CLOSE_POPUP)).click()




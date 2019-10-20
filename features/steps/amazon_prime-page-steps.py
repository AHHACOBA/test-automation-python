from behave import given, then
from selenium.webdriver.common.by import By

PRIME_TEXT_BOXES = (By.CSS_SELECTOR, "div.benefit-box-text")

@given('Open Amazon Prime page')
def open_amazon_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('Verify that there {boxes_count} benefit boxes')
def verify_prime_boxes(context, boxes_count):
    actual_boxes_count = len(context.driver.find_elements(*PRIME_TEXT_BOXES))
    assert actual_boxes_count == int(boxes_count), f'Expected {boxes_count} boxes but got {actual_boxes_count}'


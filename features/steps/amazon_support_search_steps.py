from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_INPUT_FIELD = (By.ID, 'helpsearch')
SEARCH_ICON_GO = (By.CSS_SELECTOR, 'input.a-button-input')
SEARCH_TEXT = (By.CSS_SELECTOR, 'div.help-content h1')

@given('Open Amazon Help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com//gp/help/customer/display.html')


@when('Search {help}')
def help_search(context, help):
    search_field = context.driver.find_element(*SEARCH_INPUT_FIELD)
    search_field.clear()
    search_field.send_keys(help)


@when('Click Go')
def click_go(context):
    context.driver.find_element(*SEARCH_ICON_GO).click()


@then('Verify that {help_text} text is present')
def verify_text(context, help_text):
    assert help_text in context.driver.find_element(*SEARCH_TEXT).text





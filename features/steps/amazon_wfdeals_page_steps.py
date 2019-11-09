from behave import given, then
from selenium.webdriver.common.by import By


PRODUCT_ITEM = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[6]//li")
PRODUCT_NAME = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name')


@given('Open Amazon WholeFoodsDeals page')
def open_wf_deals_page(context):
    context.driver.get(f'https://www.amazon.com/wholefoodsdeals')


@then('Verify every product on the page has a text {regular} and product name')
def verify_text_and_name(context, regular):
    webelements = context.driver.find_elements(*PRODUCT_ITEM)
    for element in webelements:
        actual_text = element.text
        #print(actual_text)
        assert regular in actual_text, f'Expected {regular}, but got {actual_text}'
        product_name = element.find_element(*PRODUCT_NAME).text
        #print('\n', product_name)
        assert product_name != '', f'Expected non-empty product name'
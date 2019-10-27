from behave import given, then
from selenium.webdriver.common.by import By


PRODUCT_ITEM = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[6]//li")
#PRODUCT_ITEM = (By.XPATH, "//div[@id = 'wfm-pmd_deals_section']//span[contains(@class, 'wfm-sales-item-card__prime-price') and contains (text(), 'PRIME')]/ancestor::div[contains(@class, 'a-text-left')]")
#PRODUCT_SALE = (By.CSS_SELECTOR, 'li.s-result-item span.a-color-error')
PRODUCT_NAME = (By.XPATH, "//div[@id = 'wfm-pmd_deals_section']//span[contains(@class, 'wfm-sales-item-card__prime-price') and contains (text(), 'PRIME')]//ancestor::div[contains(@class, 'a-text-left')]//child::span[contains(@class, 'wfm-sales-item-card__product-name')]")


@given('Open Amazon WholeFoodsDeals page')
def open_wf_deals_page(context):
    context.driver.get(f'https://www.amazon.com/wholefoodsdeals')


@then('Verify every product on the page has a text {regular} and product name')
def verify_text_and_name(context, regular):
    webelements = context.driver.find_elements(*PRODUCT_ITEM)
    actual_name = context.driver.find_elements(*PRODUCT_NAME)
    print(actual_name)
    for element in webelements:
        actual_text = context.driver.find_element(*PRODUCT_ITEM).text
        print(actual_text)
        assert regular in actual_text, f'Expected {regular}, but got {actual_text}'
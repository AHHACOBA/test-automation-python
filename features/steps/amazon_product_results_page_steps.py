from behave import when, then
from selenium.webdriver.common.by import By
#from time import sleep


TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")
PRODUCT_RESULTS = (By.XPATH, "//li[@role='listitem']//a[.//span[@class='a-price']]")
SEARCHING_PRODUCT = (By.CSS_SELECTOR, "div.sg-col-inner a.a-text-normal[href*='B00NLR1PX0']")

@when('Open the first product Search result')
def click_first_result(context):
    context.driver.find_element(*PRODUCT_RESULTS).click()

@when('Open {searching_product} product Search result')
def click_product_result(context, searching_product):
    context.driver.find_element(*SEARCHING_PRODUCT).click()


@then('Search results for {product} is shown')
def verify_result(context, product):
    #result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
      #assert result_text == '\"dress\"', f"Expected text is {product}, but got {result_text}"
    #assert product in result_text, f"Expected text is {product}, but got {result_text}"
    context.app.search_results_page.verify_result_shown(product)


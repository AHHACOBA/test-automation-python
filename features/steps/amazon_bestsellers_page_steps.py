from behave import then
from selenium.webdriver.common.by import By

from time import sleep

TOP_LINKS = (By.CSS_SELECTOR, 'div#zg_tabs a')
HEADER = (By.CSS_SELECTOR, 'div#zg_banner_text_wrapper')


@then('Clicks on each top link and verify that new page opens')
def click_through_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)
    for x in range(len(top_links)):
        link_to_click = context.driver.find_elements(*TOP_LINKS)[x]
        link_text = link_to_click.text
        link_to_click.click()
        sleep(1)
        new_text = context.driver.find_element(*HEADER).text
        assert link_text in new_text, f'Expected {link_text} to be in {new_text}'
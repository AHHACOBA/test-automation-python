from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
CLOSING_X_SIDE_SECTION = (By.ID, 'attach-close_sideSheet-link')

COLOR_OPTIONS = (By.CSS_SELECTOR, 'div#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, 'div#variation_color_name span.selection')


@when('Click Add to cart button')
def open_amazon(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@when('Close suggestion side section')
def close_side_suggestion(context):
    closing_btn = context.driver.find_elements(*CLOSING_X_SIDE_SECTION)
    if len(closing_btn) == 1:
        closing_btn[0].click()
    #else:
        #pass


@given('Open Amazon product {productid} page')
def open_item_page(context, productid):
    # context.driver.get(f'https://www.amazon.com/gp/product/{productid}')
    context.app.product_page.open_product(productid)

@when('Hoover over Add To Cart button')
def hover_add_to_cart(context):
    context.app.product_page.hover_add_to_cart()

@when('Hoover over Sales and Deals link')
def hover_over_link(context):
    context.app.product_page.hover_over_link()

@then('Verify size selection tooltip is shown')
def verify_size_tooltip(context):
    context.app.product_page.verify_size_tooltip()

@then('Verify Sales and Deals flyout is shown')
def verify_flyout_shown(context):
    context.app.product_page.verify_flyout_shown()

@then('Verify user can select through colors')
def verify_colors(context):
    #expected_colors = ['Black', 'Emerald', 'Ivory', 'Navy']
    expected_colors = ['Medium Wash', 'Dark Wash', 'Rinse']
    color_webelements = context.driver.find_elements(*COLOR_OPTIONS)
    print(color_webelements)
    for x in range(len(color_webelements)):
        color_webelements[x].click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text
        print(actual_color)
        assert actual_color == expected_colors[x], f'Expected {expected_colors[x]}, but got {actual_color}'

    #for color in color_webelements:
        #color.click()
        #actual_color = context.driver.find_element(*SELECTED_COLOR).text
        #assert actual_color == expected_colors[color_webelements.index(color)]








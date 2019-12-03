from behave import given, when, then

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


#AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
#AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")
BESTSELLERS_LINK = (By.CSS_SELECTOR, 'div#nav-xshop a[tabindex="48"]')
CART_ITEM_COUNT = (By.ID, 'nav-cart-count')
CART = (By.ID, 'nav-cart')
DEALS_UNDER_25_LINK = (By.XPATH, "//a[contains(@aria-label, 'deals under $25')]")
#HAM_MENU = (By.ID, 'nav-hamburger-menu')
ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
SEARCH_CART = (By.ID, 'nav-cart')
SIGN_IN_TOOLTIP = (By.CSS_SELECTOR, '#nav-signin-tooltip span')


@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com')
    context.app.main_page.open_page()


@when('Click Amazon Orders link')
def click_orders_link(context):
    #context.driver.find_element(*ORDERS_LINK).click()
    context.app.main_page.click_orders()


@when('Search for {product}')
def search_product(context, product):
    #search_field = context.driver.find_element(*SEARCH_INPUT)
    #search_field.clear()
    #search_field.send_keys(product)
    #context.driver.find_element(*SEARCH_ICON).click()
    context.app.main_page.search_for_keyword(product)


@when('Click Amazon Shopping Cart icon')
def click_cart(context):
    #cart_icon = context.driver.find_element(*SEARCH_CART)
    #print(cart_icon)
    #context.driver.refresh()
    #cart_icon = context.driver.find_element(*SEARCH_CART)
    #print(cart_icon)
    #cart_icon.click()
    context.app.main_page.click_cart()

@when('Click on hamburger menu')
def click_ham_menu(context):
    #context.driver.find_element(*HAM_MENU).click()
    context.app.main_page.click_ham_menu()

@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    #sleep(2)
    #context.driver.find_element(*AMAZON_MUSIC_MENU_ITEM).click()
    context.app.menu_page.click_music_menu()


@then('Verify cart has {expected_item_count} item')
def verify_item_count(context, expected_item_count):
    sleep(3)
    actual_items = context.driver.find_element(*CART_ITEM_COUNT).text
    assert actual_items == expected_item_count, f'Expected {expected_item_count}, but got {actual_items}'


@then('{expected_item_count} menu items are present')
def verify_amount_of_items(context, expected_item_count):
    expected_item_count = int(expected_item_count)
    #sleep(3)
     #print(len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)))
    #actual_item_count = len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS))
     #print(type(expected_item_count)) #-> string
     #print(type(actual_item_count)) #-> integer
     #expected_item_count = int(expected_item_count)
    #assert actual_item_count == int(expected_item_count), \
    #    f'Expected {expected_item_count} items but got {actual_item_count}'
    context.app.menu_page.verify_items_amount(expected_item_count)


@then('Verify that hamburger menu is present')
def verify_ham_menu(context):
    print('\nFIND ELEMENTSSS =>> ')
    #print(context.driver.find_elements(*HAM_MENU))
    #print(type(context.driver.find_elements(*HAM_MENU)))

    print('\nFIND ELEMENT =>> ')
    #print(context.driver.find_element(*HAM_MENU))
    #print(type(context.driver.find_element(*HAM_MENU)))

# ================================ TOOLTIP ==================================

@when('Click on Sign In btn from Sign In tooltip')
def click_signin_tooltip(context):
  context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_TOOLTIP)).click()
  #assert EC.element_to_be_clickable(SIGN_IN_TOOLTIP) == True



@then('Verify Sign In tooltip is present and clickable')
def verify_signin_tooltip_clickable(context):
  context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_TOOLTIP))
  #assert EC.element_to_be_clickable(SIGN_IN_TOOLTIP) == True


@when('Wait until Sign In tooltip disappears')
def wait_signin_tooltip_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_TOOLTIP))


@then('Verify Sign In tooltip is not clickable')
def wait_signin_tooltip_not_clicable(context):
    # Wait until NOT!
    context.driver.wait.until_not(EC.element_to_be_clickable(SIGN_IN_TOOLTIP))
    # (or the same:) assert EC.element_to_be_clickable(SIGN_IN_TOOLTIP) == False

# ============================== DEALS UNDER $25 =============================


@when('Store original windows')
def store_current_windows(context):
    context.original_window = context.driver.current_window_handle
    context.old_windows = context.driver.window_handles
    print('\noriginal_window\n', context.original_window)
    print('\nold_windows\n', context.old_windows)


@when('Click to open Deals under 25')
def click_to_open_deals_under_25(context):
    context.driver.find_element(*DEALS_UNDER_25_LINK).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    # Wait for new window
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('\ncurrent_windows\n', current_windows)
    #new_window = current_windows[1]
    #print('\nnew_window\n', new_window)

    new_windows = current_windows
    for old_window in context.old_windows:
        new_windows.remove(old_window)

    print('\nnew_windows\n', new_windows)

    # Switch to freshly opened window
    context.driver.switch_to_window(new_windows[0])


@then('User can close new window and switch back to original')
def close_and_switch_window_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)

@then('Refresh the current page')
def refresh_current_page(context):
    context.driver.refresh()

@when('Clicks on Best Sellers link on the top menu')
def click_to_bestsellers_link(context):
    context.driver.find_element(*BESTSELLERS_LINK).click()

@when('Select {department} department')
def select_department(context, department):
    context.app.main_page.select_department(department)

@then('{department} department is selected')
def verify_selected_department(context, department):
    context.app.main_page.verify_selected_department(department)







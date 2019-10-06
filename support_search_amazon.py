from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com//gp/help/customer/display.html')

# wait for 1 sec
sleep(1)

# search for "Cancel order"
search = driver.find_element(By.ID, 'helpsearch')
search.clear()
search.send_keys('Cancel order')

# wait for 1 sec
sleep(1)

# click "Go"
driver.find_element(By.XPATH, "//input[@class='a-button-input']").click()

# wait for 1 sec
sleep(1)

# verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text

driver.quit()
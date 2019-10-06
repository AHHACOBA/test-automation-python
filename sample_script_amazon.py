from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')

# wait for 1 sec
sleep(1)

#try_prime_link = driver.find_element(By.XPATH, "//a[@id='nav-link-prime']/span[@class='nav-line-2 ']")
#try_prime_link.click()
# wait for 1 sec
#sleep(1)
#driver.find_element(By.XPATH, "//div[@class='prime-button-try']").click()
# wait for 3 sec
#sleep(3)
#assert 'https://www.amazon.com/amazonprime' in driver.current_url

open_sign_in = driver.find_element(By.XPATH, "//div[@id='nav-signin-tooltip']/a")
open_sign_in.click()

# wait for 3 sec
sleep(3)

#create_acc_btn = driver.find_element(By.ID, 'createAccountSubmit').click()
# wait for 3 sec
#sleep(3)

driver.quit()
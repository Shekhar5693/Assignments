import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# username, email and phone number
first_name = "John"
last_name = "Snow"
full_name = first_name + " " + last_name
email = first_name + "." + last_name + "@example.com"
password = "admin123"
number = "1234567890"

driver = webdriver.Chrome()

driver.get("http://localhost/AD-event-management-main/admin-panel-arslaan/login.php")

sleep(3)

create_account_locator = By.PARTIAL_LINK_TEXT, "Create an Account"
driver.find_element(*create_account_locator).click()

sleep(3)

username_locator = By.CSS_SELECTOR, "input[name='username']"
fullname_locator = By.CSS_SELECTOR, "input[name='name']"
email_locator = By.CSS_SELECTOR, "input[name='email']"
password_locator = By.CSS_SELECTOR, "input[name='pass']"
number_locator = By.CSS_SELECTOR, "input[name='mobile']"
image_locator = By.CSS_SELECTOR, "input[name='image']"
submit_locator = By.CSS_SELECTOR, "button[type='submit']"

driver.find_element(*username_locator).send_keys(first_name)
driver.find_element(*fullname_locator).send_keys(full_name)
driver.find_element(*email_locator).send_keys(email)
driver.find_element(*password_locator).send_keys(password)
driver.find_element(*number_locator).send_keys(number)

driver.find_element(*image_locator).send_keys(os.getcwd() + "/admin.jpg")

sleep(3)

driver.find_element(*submit_locator).click()

sleep(3)
driver.quit()
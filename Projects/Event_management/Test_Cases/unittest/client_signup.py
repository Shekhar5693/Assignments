import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as expected



# inputs
first_name = "Baburao"
last_name = "Apte"
full_name = first_name + " " + last_name
email = first_name + "." + last_name + "@example.com"
password = "fakepassword1"
number = "1234567890"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("http://localhost/AD-event-management-main/HomePage/rishabh/")

sleep(3)

# Navigating to the client signup form
sign_up_locator = By.PARTIAL_LINK_TEXT, "SignUp"
driver.find_element(*sign_up_locator).click()

client_locator = By.CSS_SELECTOR,".ghost[id='signUp']"
driver.find_element(*client_locator).click()

sleep(5)

client_signup_button_locator = By.CSS_SELECTOR,"button[formaction='signup_client.php']"
wait.until(expected.element_to_be_clickable(client_signup_button_locator)).click()


# Filling the account form
name_field_locator = By.CSS_SELECTOR, "input[name='name']"
driver.find_element(*name_field_locator).send_keys(full_name)

username_field_locator = By.CSS_SELECTOR, "input[name='username']"
driver.find_element(*username_field_locator).send_keys(first_name)

email_field_locator = By.CSS_SELECTOR, "input[name='email']"
driver.find_element(*email_field_locator).send_keys(email)

password_field_locator = By.CSS_SELECTOR, "input[name='password']"
driver.find_element(*password_field_locator).send_keys(password)

conPwd_field_locator = By.CSS_SELECTOR, "input[name='confirm_password']"
driver.find_element(*conPwd_field_locator).send_keys(password)

number_field_locator = By.CSS_SELECTOR, "input[name='mobile_no']"
driver.find_element(*number_field_locator).send_keys(number)
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)
submit_button_locator = By.CSS_SELECTOR, "button[value='Submit']"
driver.find_element(*submit_button_locator).click()

sleep(3)
driver.quit()
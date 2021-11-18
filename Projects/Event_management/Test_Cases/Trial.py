from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open the project website
url = "http://localhost/AD-event-management-main/HomePage/rishabh/"
open = driver.get(url)


# Navigating to the client signup form
sign_up_locator = By.PARTIAL_LINK_TEXT, "SignUp"
sign_up = driver.find_element(*sign_up_locator).click()

client_locator = By.CSS_SELECTOR,".ghost[id='signUp']"
client_sign_up = driver.find_element(*client_locator).click()

client_signup_button_locator = By.CSS_SELECTOR,"button[formaction='signup_client.php']"
click = wait.until(expected.element_to_be_clickable(client_signup_button_locator)).click()

# Filling the account form
name_field_locator = By.CSS_SELECTOR, "input[name='name']"
name = driver.find_element(*name_field_locator).send_keys("Selenium")

username_field_locator = By.CSS_SELECTOR, "input[name='username']"
username = driver.find_element(*username_field_locator).send_keys("Selenium")

email_field_locator = By.CSS_SELECTOR, "input[name='email']"
email = driver.find_element(*email_field_locator).send_keys("Selenium@a.com")

password_field_locator = By.CSS_SELECTOR, "input[name='password']"
password = driver.find_element(*password_field_locator).send_keys("Selenium")

conPwd_field_locator = By.CSS_SELECTOR, "input[name='confirm_password']"
conpwd = driver.find_element(*conPwd_field_locator).send_keys("Selenium")

number_field_locator = By.CSS_SELECTOR, "input[name='mobile_no']"
number = driver.find_element(*number_field_locator).send_keys("1234567890")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)
# Click submit button
submit_button_locator = By.CSS_SELECTOR, "button[value='Submit']"
submit = driver.find_element(*submit_button_locator).click()


driver.quit()
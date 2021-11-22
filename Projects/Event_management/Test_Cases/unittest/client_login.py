from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected

username = "Baburao"
password = "fakepassword1"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("http://localhost/AD-event-management-main/HomePage/rishabh/")

sleep(3)

login_locator = By.PARTIAL_LINK_TEXT, "Login"
driver.find_element(*login_locator).click()

sleep(5)

client_locator = By.CSS_SELECTOR, ".ghost[id='signUp']"
wait.until(expected.element_to_be_clickable(client_locator)).click()

client_login_locator = By.CSS_SELECTOR, "button[formaction='login_client.php']"
wait.until(expected.element_to_be_clickable(client_login_locator)).click()

sleep(3)

username_locator = By.CSS_SELECTOR, "input[name='username']"
password_locator = By.CSS_SELECTOR, "input[name='password']"
submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
driver.find_element(*username_locator).send_keys(username)
driver.find_element(*password_locator).send_keys(password)
driver.find_element(*submit_locator).click()

sleep(3)
driver.quit()
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

sleep(3)

client_locator = By.CSS_SELECTOR, ".ghost[id='signUp']"
wait.until(expected.element_to_be_clickable(client_locator)).click()

sleep(3)

client_login_locator = By.CSS_SELECTOR, "button[formaction='login_client.php']"
wait.until(expected.element_to_be_clickable(client_login_locator)).click()

username_locator = By.CSS_SELECTOR, "input[name='username']"
password_locator = By.CSS_SELECTOR, "input[name='password']"
submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
driver.find_element(*username_locator).send_keys(username)
sleep(2)
driver.find_element(*password_locator).send_keys(password)
driver.find_element(*submit_locator).click()

sleep(3)

rsvp_locator = By.PARTIAL_LINK_TEXT, "Send RSVP"
driver.find_element(*rsvp_locator).click()

sleep(3)

invite_locator = By.PARTIAL_LINK_TEXT, "Single Invite"
driver.find_element(*invite_locator).click()

driver.switch_to.window(driver.window_handles[1])

name_locator = By.CSS_SELECTOR, "input#name"
driver.find_element(*name_locator).send_keys("Raj")

yes_locator = By.CSS_SELECTOR, "label[for='Yes']"
driver.find_element(*yes_locator).click()

cuisine_locator = By.CSS_SELECTOR, "label[for='Italian']"
driver.find_element(*cuisine_locator).click()

otherCuisine_locator = By.CSS_SELECTOR, "#otherCuisine"
driver.find_element(*otherCuisine_locator).send_keys("N.A.")

driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
sleep(2)

specialMessage_locator = By.CSS_SELECTOR, "#specialMsg"
driver.find_element(*specialMessage_locator).send_keys("Congratulations")

sleep(3)

submit_locator2 = By.XPATH, "//button[normalize-space()='Submit']"
driver.find_element(*submit_locator2).click()

sleep(3)
driver.quit()
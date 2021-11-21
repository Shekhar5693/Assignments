from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected

username = "Mamooty"
password = "fakepassword1"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("http://localhost/AD-event-management-main/HomePage/rishabh/")

sleep(3)
	
#-------------------------------------------NAVIGATING TO SITE AND LOGIN PAGE--------------------------------------------#
	
login_locator = By.PARTIAL_LINK_TEXT, "Login"
driver.find_element(*login_locator).click()

sleep(5)

client_login_locator = By.CSS_SELECTOR, "button[formaction='login_event-manager.php']"
wait.until(expected.element_to_be_clickable(client_login_locator)).click()

sleep(3)

name_locator = By.CSS_SELECTOR, "input[name='username']"
driver.find_element(*name_locator).send_keys(username)

password_locator = By.CSS_SELECTOR,"input[name='password']"
driver.find_element(*password_locator).send_keys(password)

submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
driver.find_element(*submit_locator).click()

sleep(3)
driver.quit()
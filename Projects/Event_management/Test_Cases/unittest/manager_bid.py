from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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


#-------------------------------------------Bidding-----------------------------------------------------#
bid_button_locator = By.XPATH, "//tbody/tr[2]/td[10]/button[1]"
driver.find_element(*bid_button_locator).click()
sleep(2)
 
price_locator = By.CSS_SELECTOR, "input[name='price']"
price = driver.find_element(*price_locator)
action:ActionChains = ActionChains(driver)
action.click(price)
action.send_keys("5000")
action.perform()

note_locator = By.CSS_SELECTOR, "#note"
note = driver.find_element(*note_locator)
action:ActionChains = ActionChains(driver)
action.click(note)
action.send_keys("I filled it via selenium")
action.perform()

sleep(3)

submit_locator = By.CSS_SELECTOR, "input[name='abc']"
driver.find_element(*submit_locator).click()

sleep(3)
driver.quit()
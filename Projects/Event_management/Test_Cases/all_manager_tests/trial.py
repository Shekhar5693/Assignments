from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


	
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

username = "Mamooty"
password = "fakepassword1"
client_account = "Lakshay"
wrong_username = "Mamoot"
wrong_password = "fakepassword"

#-------------------------------------------------TESTS-----------------------------------------------------------------#


# test for successful logging in and event creation


#-------------------------------------------NAVIGATING TO SITE AND LOGIN PAGE--------------------------------------------#	

driver.get("http://localhost/AD-event-management-main/HomePage/rishabh/")
	

login_locator = By.PARTIAL_LINK_TEXT, "Login"
driver.find_element(*login_locator).click()

client_login_locator = By.CSS_SELECTOR, "button[formaction='login_event-manager.php']"
wait.until(expected.element_to_be_clickable(client_login_locator)).click()


name_locator = By.CSS_SELECTOR, "input[name='username']"
driver.find_element(*name_locator).send_keys(username)

password_locator = By.CSS_SELECTOR,"input[name='password']"
driver.find_element(*password_locator).send_keys(password)

submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
driver.find_element(*submit_locator).click()

bid_button_locator = By.XPATH, "//tbody/tr[2]/td[10]/button[1]"
driver.find_element(*bid_button_locator).click()
 
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

submit_locator = By.CSS_SELECTOR, "input[name='abc']"
driver.find_element(*submit_locator).click()


text = driver.find_elements_by_class_name,("body").text
print(text)

driver.quit()
#-------------------------------------------LOGIN AND EVENT CREATION-----------------------------------------------------#
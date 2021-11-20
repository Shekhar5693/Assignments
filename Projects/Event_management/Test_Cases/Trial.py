from webdriver_helpers import *



driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
	


username = "Lakshay"
password = "fakepassword1"
number = random.randint(0,10)
budget = random.randint(5000,10000)


driver.get("http://localhost/AD-event-management-main/HomePage/rishabh/")
	
	
login_locator = By.PARTIAL_LINK_TEXT, "Login"
driver.find_element(*login_locator).click()
		
client_locator = By.CSS_SELECTOR, ".ghost[id='signUp']"
wait.until(expected.element_to_be_clickable(client_locator)).click()

client_login_locator = By.CSS_SELECTOR, "button[formaction='login_client.php']"
wait.until(expected.element_to_be_clickable(client_login_locator)).click()

	
username_locator = By.CSS_SELECTOR, "input[name='username']"
password_locator = By.CSS_SELECTOR, "input[name='password']"
submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
driver.find_element(*username_locator).send_keys(username)
driver.find_element(*password_locator).send_keys(password)
driver.find_element(*submit_locator).click()

	 
event_button_locator = By.PARTIAL_LINK_TEXT, "Post event"
driver.find_element(*event_button_locator).click()

name_field_locator = By.CSS_SELECTOR, "input[name='name']"
driver.find_element(*name_field_locator).send_keys("Lakshay")

select_surat = By.CSS_SELECTOR, "[id='floatingSelect'] [value='Surat']"
driver.find_element(*select_surat).click()

name_field_locator = By.CSS_SELECTOR, "input[name='attendees']"
driver.find_element(*name_field_locator).send_keys(number)
		
name_field_locator = By.CSS_SELECTOR, "input[name='budget']"
driver.find_element(*name_field_locator).send_keys(budget)

venue_radio_locator = By.CSS_SELECTOR, "input[type='radio'][name='venue_type']"
venue_names = driver.find_elements(*venue_radio_locator)
print (venue_names)
a=[]
for i in venue_names:
    a.append(i.get_attribute("value"))
print(a)
b = random.choice(a)

html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.PAGE_DOWN)
sleep(2)

venue_select = By.CSS_SELECTOR, "input[type=radio][value = '{}']".format(b)
driver.find_element(*venue_select).click()

date = By.CSS_SELECTOR, "input[name='time']"
d = driver.find_element(*date)
action:ActionChains = ActionChains(driver)
action.click(d)
action.send_keys("30112021")
action.send_keys(Keys.TAB)
action.send_keys("1130")
action.send_keys("P")
action.perform()

sleep(5)
driver.quit()
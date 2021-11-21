import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as expected


# inputs
username = "client"
password = "123456q"
number = random.randint(0,10)
budget = random.randint(5000,10000)

#-------------------------------------------NAVIGATING TO SITE AND LOGIN PAGE--------------------------------------------#	
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

#-------------------------------------------LOGIN AND EVENT CREATION-----------------------------------------------------#

username_locator = By.CSS_SELECTOR, "input[name='username']"
password_locator = By.CSS_SELECTOR, "input[name='password']"
submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
driver.find_element(*username_locator).send_keys(username)
driver.find_element(*password_locator).send_keys(password)
driver.find_element(*submit_locator).click()

sleep(5)

event_button_locator = By.PARTIAL_LINK_TEXT, "Post event"
driver.find_element(*event_button_locator).click()

name_field_locator = By.CSS_SELECTOR, "input[name='name']"
driver.find_element(*name_field_locator).send_keys(username)

select_surat = By.CSS_SELECTOR, "[id='floatingSelect'] [value='Surat']"
driver.find_element(*select_surat).click()

name_field_locator = By.CSS_SELECTOR, "input[name='attendees']"
driver.find_element(*name_field_locator).send_keys(number)

name_field_locator = By.CSS_SELECTOR, "input[name='budget']"
driver.find_element(*name_field_locator).send_keys(budget)
sleep(2)

html = driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
sleep(1)

venue_names_locator = By.CSS_SELECTOR, "input[type='radio'][name='venue_type']"
venue_names = driver.find_elements(*venue_names_locator)
venue_names_list = []
for i in venue_names:
    venue_names_list.append(i.get_attribute("value"))
    venue_name = random.choice(venue_names_list)
venue_select = By.CSS_SELECTOR, "input[type=radio][value = '{}']".format(venue_name)
driver.find_element(*venue_select).click()

duration_locator = By.CSS_SELECTOR, "input[name='duration']"
driver.find_element(*duration_locator).send_keys("2")

date_locator = By.CSS_SELECTOR, "input[name='time']"
date = driver.find_element(*date_locator)
action:ActionChains = ActionChains(driver)
action.click(date)
action.send_keys("30112021")
action.send_keys(Keys.TAB)
action.send_keys("0630")
action.send_keys("P")
action.perform()

event_locator = By.CSS_SELECTOR, "input[type='radio'][name='event_type']"
event_names = driver.find_elements(*event_locator)
event_list = []
for i in event_names:
    event_list.append(i.get_attribute("value"))
    event_name = random.choice(event_list)
event_select = By.CSS_SELECTOR, "input[type=radio][value = '{}']".format(event_name)
driver.find_element(*event_select).click()

description_locator = By.CSS_SELECTOR, ".form-control[name='description']"
driver.find_element(*description_locator).send_keys("Need manager for {} celebration.".format(event_name))
sleep(2)

html = driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
sleep(1)

submit_locator = By.CSS_SELECTOR, "input[name='submit']"
driver.find_element(*submit_locator).click()

sleep(3)
driver.quit()
from webdriver_helpers import *

fake = Faker("en_IN")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
action:ActionChains = ActionChains(driver)

URl = "http://www.tutorialsninja.com/demo/"
driver.get(URl)

search_locator = By.CSS_SELECTOR, "input[name='search']"
phone = "iphone"

#iphones
search = driver.find_element(*search_locator)
action.click(search)
action.send_keys(phone)
action.send_keys(Keys.ENTER)
action.perform()
sleep(3)

driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)
sleep(2)

iphone_locator = By.CSS_SELECTOR, "img[title='iPhone']"
driver.find_element(*iphone_locator).click()

quantity_locator = By.CSS_SELECTOR, "#input-quantity"
quantity = driver.find_element(*quantity_locator)
quantity.send_keys(Keys.BACKSPACE)
quantity.send_keys("2")
sleep(2)

#screenshot
driver.save_screenshot("ss.png")
sleep(2)

#going back home
home = By.XPATH, "//a[normalize-space()='Your Store']"
driver.find_element(*home).click()
sleep(2)

#laptop
laptop = driver.find_element(*search_locator)
laptop.send_keys("HP lp3065")
sleep(2)
laptop.send_keys(Keys.ENTER)
sleep(3)

driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)
sleep(2)

laptop_locator = By.CSS_SELECTOR, "img[title='HP LP3065']"
driver.find_element(*laptop_locator).click()
sleep(3)

date_locator = By.CSS_SELECTOR, "#input-option225"
date = driver.find_element(*date_locator)
date.clear()
date.send_keys("2022-12-31")
sleep(3)

add_to_cart = By.CSS_SELECTOR, "#button-cart"
driver.find_element(*add_to_cart).click()
sleep(2)

# navigate to cart
cart_locator = By.CSS_SELECTOR, "#cart-total"
driver.find_element(*cart_locator).click()
sleep(2)

checkout_locator = By.XPATH, "//strong[normalize-space()='Checkout']"
wait.until(expected.element_to_be_clickable(checkout_locator)).click()
sleep(3)

#guest checkout
guest_locator = By.CSS_SELECTOR, "input[type='radio'][value='guest']"
driver.find_element(*guest_locator).click()
sleep(2)

continue_locator = By.CSS_SELECTOR, "#button-account"
driver.find_element(*continue_locator).click()
sleep(2)

#Initializing variables for guest account
firstname = fake.first_name()
lastname = fake.last_name()
email = fake.email()
phone = "1234567890"
address = fake.address()
city = fake.city()
postcode = fake.postcode()
country = By.CSS_SELECTOR, "#input-payment-country [value='99']"
state = By.CSS_SELECTOR, "#input-payment-zone [value='1475']"

#filling guest account form
firstname_locator = By.CSS_SELECTOR, "#input-payment-firstname"
driver.find_element(*firstname_locator).send_keys(firstname)

lastname_locator = By.CSS_SELECTOR, "#input-payment-lastname"
driver.find_element(*lastname_locator).send_keys(lastname)

email_locator = By.CSS_SELECTOR, "#input-payment-email"
driver.find_element(*email_locator).send_keys(email)

phone_locator = By.CSS_SELECTOR, "#input-payment-telephone"
driver.find_element(*phone_locator).send_keys(phone)

address_locator = By.CSS_SELECTOR, "#input-payment-address-1"
driver.find_element(*address_locator).send_keys(address)

city_locator = By.CSS_SELECTOR, "#input-payment-city"
driver.find_element(*city_locator).send_keys(city)

postcode_locator = By.CSS_SELECTOR, "#input-payment-postcode"
driver.find_element(*postcode_locator).send_keys(postcode)

driver.find_element(*country).click()
wait.until(expected.visibility_of_element_located(state)).click()
sleep(3)

continue_locator2 = By.CSS_SELECTOR, "input#button-guest"
driver.find_element(*continue_locator2).click()
sleep(2)

continue_locator3 = By.CSS_SELECTOR, "input#button-shipping-method"
wait.until(expected.element_to_be_clickable(continue_locator3)).click()
sleep(2)

terms_conditions = By.CSS_SELECTOR, "input[value='1'][name='agree']"
wait.until(expected.element_to_be_clickable(terms_conditions)).click()
sleep(2)

continue_locator4 = By.CSS_SELECTOR, "input#button-payment-method"
wait.until(expected.element_to_be_clickable(continue_locator4)).click()
sleep(2)

price_locator = By.XPATH, "//*[@id='collapse-checkout-confirm']/div/div[1]/table/tfoot/tr[3]/td[2]"
price = driver.find_element(*price_locator).text
print("Total price to be paid is:",price)

confirm_locator = By.CSS_SELECTOR, "input#button-confirm"
driver.find_element(*confirm_locator).click()
sleep(2)

confirmation_locator = By.CSS_SELECTOR, "#content > h1"
confirmation = driver.find_element(*confirmation_locator).text
print("Message:", confirmation)

driver.quit()
screenshot = Image.open("ss.png")
screenshot.show()
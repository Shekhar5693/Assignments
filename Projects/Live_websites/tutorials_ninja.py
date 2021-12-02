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

iphone_locator = By.CSS_SELECTOR, "img[title='iPhone']"
driver.find_element(*iphone_locator).click()

quantity_locator = By.CSS_SELECTOR, "#input-quantity"
quantity = driver.find_element(*quantity_locator)
quantity.send_keys(Keys.BACKSPACE)
quantity.send_keys("2")

#screenshot
driver.save_screenshot("ss.png")

#going back home
home = By.XPATH, "//a[normalize-space()='Your Store']"
driver.find_element(*home).click()

#laptop
laptop = driver.find_element(*search_locator)
laptop.send_keys("HP lp3065")
laptop.send_keys(Keys.ENTER)
sleep(3)

driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)
sleep(2)
laptop_locator = By.CSS_SELECTOR, "img[title='HP LP3065']"
driver.find_element(*laptop_locator).click()
sleep(3)

date_loator = By.CSS_SELECTOR, "#input-option225"
date = driver.find_element(*date_loator)
date.clear()
date.send_keys("2022-12-31")
sleep(3)

add_to_cart = By.CSS_SELECTOR, "#button-cart"
driver.find_element(*add_to_cart).click()

# navigate to cart
cart_locator = By.CSS_SELECTOR, "#cart-total"
driver.find_element(*cart_locator).click()

checkout_locator = By.XPATH, "//strong[normalize-space()='Checkout']"
wait.until(expected.element_to_be_clickable(checkout_locator)).click()
sleep(3)

#guest checkout
guest_locator = By.CSS_SELECTOR, "input[type='radio'][value='guest']"
driver.find_element(*guest_locator).click()

continue_locator = By.CSS_SELECTOR, "#button-account"
driver.find_element(*continue_locator).click()

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


driver.quit()
#screenshot = Image.open("ss.png")
#screenshot.show()
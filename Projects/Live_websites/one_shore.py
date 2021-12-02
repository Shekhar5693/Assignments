from webdriver_helpers import *


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

url = "https://shop.one-shore.com/index.php"
driver.get(url)

search_locator = By.CSS_SELECTOR, "input[name='s']"
driver.find_element(*search_locator).send_keys("hummingbird printed sweater")
sleep(2)

select_sweater = By.CSS_SELECTOR, "img[alt='Brown bear printed sweater']"
driver.find_element(*select_sweater).click()

select_size = By.CSS_SELECTOR, "#group_1 [value = '3']"
driver.find_element(*select_size).click()
sleep(3)

increase_quantity = By.CSS_SELECTOR, ".material-icons.touchspin-up"
increase = driver.find_element(*increase_quantity)
for i in range (4):
    increase.click()
sleep(3)

add_to_cart_locator = By.CSS_SELECTOR, ".add-to-cart"
driver.find_element(*add_to_cart_locator).click()
sleep(3)

proceed_checkout_locator = By.CSS_SELECTOR, "a[class='btn btn-primary']"
wait.until(expected.element_to_be_clickable(proceed_checkout_locator)).click()
sleep(3)

total = driver.find_element(By.CSS_SELECTOR, ("div[class='cart-summary-line cart-total'] span[class='value']")).text
print("Total bill is:", total)

driver.quit()
#py.test exampletest.py -s
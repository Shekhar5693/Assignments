from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
start = By.CSS_SELECTOR, "#start > button"
finish = By.CSS_SELECTOR, "#finish > h4"

try:
    driver.find_element(*start).click()
    wait = WebDriverWait(driver, 10)
    text = wait.until(expected.visibility_of_element_located(finish)).text
    print(text)
    
finally:    
    driver.quit()

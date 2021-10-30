from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://shop.one-shore.com/index.php")

driver.find_element_by_name("s").click()
driver.find_element_by_name("s").send_keys("mug")
driver.find_element_by_xpath("//button[@type='submit']").click()

elements = driver.find_elements(By.CLASS_NAME, "product-description")


for element in elements:   
    name = element.find_element(By.CLASS_NAME, "product-title").text
    price = element.find_element(By.CLASS_NAME, "price").text 
        
    print("Mug name: {} \nPrice: {}".format(name,price))
                
driver.quit()
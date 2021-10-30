from time import sleep
from selenium import webdriver
from socket import gethostname
#from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()

if "console" in gethostname():
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options = chrome_options)

driver.get("https://shop.one-shore.com/index.php")
driver.find_element_by_css_selector("div[id='contact-link'] a").click()
#driver.find_element_by_css_selector(".buttonText").click()
driver.find_element_by_name("from").click()
driver.find_element_by_name("from").send_keys("shekhu506@outlook.com")
driver.find_element_by_css_selector("textarea[placeholder='How can we help?']").click()
driver.find_element_by_css_selector("textarea[placeholder='How can we help?']").send_keys("Dont mind me! Just testing Selenium.")
driver.find_element_by_xpath("//input[@name='submitMessage']").click()
a = driver.find_element_by_css_selector(".col-xs-12 li").text 
if a == "Your message has been successfully sent to our team.":
    print("Message was sent")
else:
    print("Message was not sent")


#sleep(2)
driver.quit()
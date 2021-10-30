import pytest
from time import sleep
from selenium import webdriver

class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown(self):
        self.driver.quit()

    def test_SeleniumForm(self):
        
        url = "https://shop.one-shore.com/index.php"
        self.driver.get(url)
         
        contact_locator = "div[id='contact-link'] a"
        contact = self.driver.find_element_by_css_selector(contact_locator)
        contact.click()
 
        subject_locator = ".contact-form > form select[name=id_contact]"
        webmaster_locator = "option[value='1']"
        subject = self.driver.find_element_by_css_selector(subject_locator)
        subject.find_element_by_css_selector(webmaster_locator).click()
        
        email_locator = "//section[@class='contact-form']//input[@type='email']"
        my_email = "abc@def.com"
        email = self.driver.find_element_by_xpath(email_locator)
        email.send_keys(my_email)

        message_locator = "textarea[placeholder='How can we help?']"
        my_message = "Dont mind me! Just testing Selenium."
        message = self.driver.find_element_by_css_selector(message_locator)
        message.send_keys(my_message)

        sleep(3)
        
        submit_locator = "//input[@name='submitMessage']"
        submit = self.driver.find_element_by_xpath(submit_locator)
        submit.click()
        
        assert self.driver.find_element_by_css_selector(".col-xs-12 li").text == "Your message has been successfully sent to our team."


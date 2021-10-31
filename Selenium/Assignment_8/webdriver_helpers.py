import os

from time import sleep
from socket import gethostname
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


def running_on_python_anywhere():
	if "console" in gethostname():
		return True
	return False

def get_chrome_options():
	chrome_options = webdriver.ChromeOptions()

	if running_on_python_anywhere():
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-gpu")
	return chrome_options
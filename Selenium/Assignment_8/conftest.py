import pytest
from socket import gethostname
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def running_on_python_anywhere():
	if "console" in gethostname():
		return True
	return False

@pytest.fixture(autouse=True)
def chrome_options():
	chrome_options = webdriver.ChromeOptions()
	if running_on_python_anywhere():
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-gpu")
	return chrome_options

@pytest.fixture()
def driver(chrome_options):
	print(chrome_options)
	driver = webdriver.Chrome(options=chrome_options)
	yield driver
	sleep(4)
	driver.quit()

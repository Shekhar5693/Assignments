import pytest
from time import sleep
from selenium import webdriver

@pytest.fixture()
def driver():
	driver = webdriver.Chrome()
	yield driver
	sleep(4)
	driver.quit()

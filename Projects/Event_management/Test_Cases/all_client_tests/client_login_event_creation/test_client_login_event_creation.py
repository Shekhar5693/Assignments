import pytest
import random
from create_event import Test_login_event_creation


username = "Lakshay"
password = "fakepassword1"
manager_account = "Mamooty"
wrong_username = "Lakshat"
wrong_password = "fakepassword"
number = random.randint(0,10)
budget = random.randint(5000,10000)

@pytest.fixture()
def create_event(driver):
    return Test_login_event_creation(driver)

def test_login_wrong_username(create_event:Test_login_event_creation):
	create_event.project_site()
	create_event.client_login()
	assert create_event.login_wrong_username(wrong_username, password) == "Invalid username."

	

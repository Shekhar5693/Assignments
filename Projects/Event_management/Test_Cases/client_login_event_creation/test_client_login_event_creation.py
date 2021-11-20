import pytest
from webdriver_helpers import *

from create_event import Test_login_event_creation

@pytest.fixture
def account(self):
	account = SimpleNamespace()
	account.username = "Lakshay"
	account.password = "fakepassword1"
	account.manager_account = "Mamooty"
	account.wrong_username = "Lakshat"
	account.wrong_password = "fakepassword"
	account.number = random.randint(0,10)
	account.budget = random.randint(5000,10000)
	self.account = account
	return account

@pytest.fixture()
def create_event(driver):
    return Test_login_event_creation(driver)

def test_login_wrong_username(create_event:Test_login_event_creation):
	create_event.project_site()
	create_event.client_login()
	assert create_event.login_wrong_username(account.wrong_username, account.password) == "Invalid username."

	

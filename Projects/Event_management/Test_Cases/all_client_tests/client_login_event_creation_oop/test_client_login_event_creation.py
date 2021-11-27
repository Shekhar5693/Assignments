import pytest
import random
from create_event import login_event_creation

# Login information for the tests
username = "Lakshay"
password = "fakepassword1"
manager_ = "Mamooty"
wrong_username = "Lakshat"
wrong_password = "fakepassword"
number = random.randint(0,10)
budget = random.randint(5000,10000)

@pytest.fixture()
def create_event(driver):
    return login_event_creation(driver)

# Test for trying to log in using wrong user name
def test_login_wrong_username(create_event:login_event_creation):
	create_event.project_site()
	create_event.client_login()
	assert create_event.login_wrong_username(wrong_username, password) == "Invalid username."

# Test for trying to login with wrong password	
def test_login_wrong_password(create_event:login_event_creation):
	create_event.project_site()
	create_event.client_login()
	assert create_event.login_wrong_password(username,wrong_password) == "Invalid password."	

# Test for trying to log in with manager account
def test_login_using_manager(create_event:login_event_creation):
	create_event.project_site()
	create_event.client_login()
	assert create_event.login_manager_account(manager_,password) == "Invalid username."

# test for successful logging in and event creation
def test_client_login_event_creation(create_event:login_event_creation):
	create_event.project_site()
	create_event.client_login()
	create_event.log_in(username, password)
	assert create_event.logged_in() == "Client Dashboard"
	create_event.fill_event_form(username, number, budget)
	assert create_event.event_created() == "Event created successfully!"

# Test for creating rsvp
def test_rsvp(create_event:login_event_creation):
	create_event.project_site()
	create_event.client_login()
	create_event.log_in(username, password)
	create_event.rsvp()
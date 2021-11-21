import pytest
import random
from faker import Faker
from client_signup import UserAccount


fake = Faker("en_IN")

first_name = fake.first_name()
last_name = fake.last_name()
full_name = first_name + " " + last_name
email = first_name + "." + last_name + "@example.com"
password = "fakepassword1"
number = "1234567890"

# generating the username, email and phone number using faker
@pytest.fixture
def client_signup(driver):
    return UserAccount(driver)

def test_create_client_account(client_signup:UserAccount):
    client_signup.project_site()
    client_signup.client_signup_form()
    client_signup.enter_name(full_name)
    client_signup.enter_username(first_name)
    client_signup.enter_email(email)
    client_signup.enter_password(password)
    client_signup.enter_con_password(password)
    client_signup.enter_number(number)
    client_signup.click_submit_button()
    assert client_signup.created() == "Login"

    client_signup.log_in(first_name, password)
    assert client_signup.logged_in() == "Client Dashboard"
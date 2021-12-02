from webdriver_helpers import *

class TestUserAccount:

    @pytest.fixture(autouse=True)
    def setup(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fake = Faker("en_IN")

# generating the username, email and phone number using faker
    @pytest.fixture
    def account(self):
        account = SimpleNamespace()
        account.first_name = self.fake.first_name()
        account.last_name = self.fake.last_name()
        account.full_name = account.first_name + " " + account.last_name
        account.email = account.first_name + "." + account.last_name + "@example.com"
        account.password = "fakepassword1"
        account.number = "1234567890"
        self.account = account
        return account

    def test_create_manager_account(self, account):
        self.project_site()
        self.manager_signup_form()
        self.enter_name(account.full_name)
        self.enter_username(account.first_name)
        self.enter_email(account.email)
        self.enter_password(account.password)
        self.enter_con_password(account.password)
        self.enter_number(account.number)
        self.click_submit_button()
        assert self.created() == "Login"

        self.log_in(account.first_name, account.password)
        assert self.logged_in() == "managerdash"

        self.bid()

# Open the project website
    def project_site(self):
        self.driver.get("http://localhost/AD-event-management-main/HomePage/rishabh/")

# Navigating to the manager signup form
    def manager_signup_form(self):
        sign_up_locator = By.PARTIAL_LINK_TEXT, "SignUp"
        self.driver.find_element(*sign_up_locator).click()

        manager_signup_button_locator = By.CSS_SELECTOR,"button[formaction='signup_event-manager.php']"
        self.driver.find_element(*manager_signup_button_locator).click()

# Filling the account form
    def enter_name(self,fullname):
        name_field_locator = By.CSS_SELECTOR, "input[name='name']"
        self.driver.find_element(*name_field_locator).send_keys(fullname)

    def enter_username(self,username):
        username_field_locator = By.CSS_SELECTOR, "input[name='username']"
        self.driver.find_element(*username_field_locator).send_keys(username)

    def enter_email(self,email):
        email_field_locator = By.CSS_SELECTOR, "input[name='email']"
        self.driver.find_element(*email_field_locator).send_keys(email)

    def enter_password(self,password):
        password_field_locator = By.CSS_SELECTOR, "input[name='password']"
        self.driver.find_element(*password_field_locator).send_keys(password)

    def enter_con_password(self,password):
        conPwd_field_locator = By.CSS_SELECTOR, "input[name='confirm_password']"
        self.driver.find_element(*conPwd_field_locator).send_keys(password)

    def enter_number(self,number):
        number_field_locator = By.CSS_SELECTOR, "input[name='mobile_no']"
        self.driver.find_element(*number_field_locator).send_keys(number)

    def click_submit_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        submit_button_locator = By.CSS_SELECTOR, "button[value='Submit']"
        self.driver.find_element(*submit_button_locator).click()

    def created(self):
        return self.driver.title

    def log_in(self, username, password):
        username_locator = By.CSS_SELECTOR, "input[name='username']"
        password_locator = By.CSS_SELECTOR, "input[name='password']"
        submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
        self.driver.find_element(*username_locator).send_keys(username)
        self.driver.find_element(*password_locator).send_keys(password)
        self.driver.find_element(*submit_locator).click()

    def logged_in(self):
        return self.driver.title

    #-------------------------------------------Bidding-----------------------------------------------------#
    def bid(self):
        bid_button_locator = By.XPATH, "//tbody/tr[2]/td[10]/button[1]"
        self.driver.find_element(*bid_button_locator).click()
        sleep(2)
               
        price_locator = By.CSS_SELECTOR, "input[name='price']"
        price = self.driver.find_element(*price_locator)
        action:ActionChains = ActionChains(self.driver)
        action.click(price)
        action.send_keys("5000")
        action.perform()

        note_locator = By.CSS_SELECTOR, "#note"
        note = self.driver.find_element(*note_locator)
        action:ActionChains = ActionChains(self.driver)
        action.click(note)
        action.send_keys("I filled it via selenium")
        action.perform()

        submit_locator = By.CSS_SELECTOR, "input[name='abc']"
        self.driver.find_element(*submit_locator).click()
        


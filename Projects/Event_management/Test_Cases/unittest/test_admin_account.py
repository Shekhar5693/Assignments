from webdriver_helpers import *

class TestCreateAccount:
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
        account.password = "admin123"
        account.number = "1234567890"
        self.account = account
        return account

    def test_create_account(self,account):
        self.admin_site()
        self.create_account()
        self.fill_form(account.first_name, account.full_name, account.email, account.password, account.number)
        assert self.sent_for_aproval() == "User sent for approval..."
    
    def admin_site(self):
        self.driver.get("http://localhost/AD-event-management-main/admin-panel-arslaan/login.php")

    def create_account(self):
        create_account_locator = By.PARTIAL_LINK_TEXT, "Create an Account"
        self.driver.find_element(*create_account_locator).click()

    def fill_form(self, firstname, name, email, password, number):
        username_locator = By.CSS_SELECTOR, "input[name='username']"
        fullname_locator = By.CSS_SELECTOR, "input[name='name']"
        email_locator = By.CSS_SELECTOR, "input[name='email']"
        password_locator = By.CSS_SELECTOR, "input[name='pass']"
        number_locator = By.CSS_SELECTOR, "input[name='mobile']"
        image_locator = By.CSS_SELECTOR, "input[name='image']"
        submit_locator = By.CSS_SELECTOR, "button[type='submit']"

        self.driver.find_element(*username_locator).send_keys(firstname)
        self.driver.find_element(*fullname_locator).send_keys(name)
        self.driver.find_element(*email_locator).send_keys(email)
        self.driver.find_element(*password_locator).send_keys(password)
        self.driver.find_element(*number_locator).send_keys(number)
        self.driver.find_element(*image_locator).send_keys(os.getcwd() + "/admin.jpg")
        sleep(2)
        self.driver.find_element(*submit_locator).click()

    def sent_for_aproval(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[role='alert'] strong").text
        
from webdriver_helpers import *

class Test_login_event_creation:
    @pytest.fixture(autouse=True)
    def setup(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
	
    @pytest.fixture
    def account(self):
        account = SimpleNamespace()
        account.username = "Mamooty"
        account.password = "fakepassword1"
        account.client_account = "Lakshay"
        account.wrong_username = "Mamoot"
        account.wrong_password = "fakepassword"
        self.account = account
        return account

#-------------------------------------------------TESTS-----------------------------------------------------------------#
# test for successful logging in and event creation
    def test_client_login_event_creation(self, account):
        self.project_site()
        self.manager_login()
        self.login(account.username, account.password)
        assert self.logged_in() == "managerdash"
        self.bid()

# Test for trying to log in with manager account    
    def test_login_using_client(self,account):
        self.project_site()
        self.manager_login()
        assert self.login_client_account(account.client_account,account.password) == "Invalid username ."

# Test for trying to login with wrong password
    def test_login_wrong_password(self, account):
        self.project_site()
        self.manager_login()
        assert self.login_wrong_password(account.username,account.wrong_password) == "Invalid password."

# Test for trying to log in using wrong user name
    def test_login_wrong_username(self, account):
        self.project_site()
        self.manager_login()
        assert self.login_wrong_username(account.wrong_username, account.password) == "Invalid username ."

#-------------------------------------------NAVIGATING TO SITE AND LOGIN PAGE--------------------------------------------#	
    def project_site(self):
        self.driver.get("http://localhost/AD-event-management-main/HomePage/rishabh/")
	
    def manager_login(self):
        login_locator = By.PARTIAL_LINK_TEXT, "Login"
        self.driver.find_element(*login_locator).click()

        client_login_locator = By.CSS_SELECTOR, "button[formaction='login_event-manager.php']"
        self.wait.until(expected.element_to_be_clickable(client_login_locator)).click()
        
    def login(self, username, password):
        name_locator = By.CSS_SELECTOR, "input[name='username']"
        self.driver.find_element(*name_locator).send_keys(username)

        password_locator = By.CSS_SELECTOR,"input[name='password']"
        self.driver.find_element(*password_locator).send_keys(password)

        submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
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

#-------------------------------------------WRONG USER NAME-------------------------------------------------------------#
    def login_wrong_username(self,uname,pwd):
        username_locator = By.CSS_SELECTOR, "input[name='username']"
        password_locator = By.CSS_SELECTOR, "input[name='password']"
        submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
        alert = By.CSS_SELECTOR, ".alert"
        self.driver.find_element(*username_locator).send_keys(uname)
        self.driver.find_element(*password_locator).send_keys(pwd)
        self.driver.find_element(*submit_locator).click()
        return self.driver.find_element(*alert).text

#--------------------------------------------WRONG PASSWORD-------------------------------------------------------------#	
    def login_wrong_password(self,uname,pwd):
        username_locator = By.CSS_SELECTOR, "input[name='username']"
        password_locator = By.CSS_SELECTOR, "input[name='password']"
        submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
        alert = By.CSS_SELECTOR, ".alert"
        self.driver.find_element(*username_locator).send_keys(uname)
        self.driver.find_element(*password_locator).send_keys(pwd)
        self.driver.find_element(*submit_locator).click()
        return self.driver.find_element(*alert).text

#--------------------------------------------CLIENT ACCOUNT-------------------------------------------------------------#
    def login_client_account(self,uname,pwd):
        username_locator = By.CSS_SELECTOR, "input[name='username']"
        password_locator = By.CSS_SELECTOR, "input[name='password']"
        submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
        alert = By.CSS_SELECTOR, ".alert"
        self.driver.find_element(*username_locator).send_keys(uname)
        self.driver.find_element(*password_locator).send_keys(pwd)
        self.driver.find_element(*submit_locator).click()		
        return self.driver.find_element(*alert).text
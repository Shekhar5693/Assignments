from webdriver_helpers import *
sys.path.append("/Automation Assignments/today")
from credentials import *

class TestSendEmail:
    
    @pytest.fixture(autouse=True)
    def setup(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def test_send_email(self):
        self.open()
        self.login()
        self.compose()
    
    def open(self):
        self.driver.get("https://gmail.com")
    
    def login(self):
        email_id = email
        pwd = password
        input_field_locator = By.CSS_SELECTOR, "#identifierId"
        next_locator = By.XPATH, "//span[normalize-space()='Next']"
        pwd_locator = By.CSS_SELECTOR, "input[name='password']"
        
        self.driver.find_element(*input_field_locator).send_keys(email_id)
        sleep(3)
        self.driver.find_element(*next_locator).click()
        sleep(3)
        self.driver.find_element(*pwd_locator).send_keys(pwd)
        self.driver.find_element(*next_locator).click()
    
    def compose(self):
        compose_locator = By.CSS_SELECTOR, ".T-I.T-I-KE.L3"
        self.wait.until(expected.element_to_be_clickable(compose_locator)).click()
        sleep(3)

        to = By.CSS_SELECTOR, "textarea[name='to']"
        subject = By.CSS_SELECTOR, "input[name='subjectbox']"
        body = By.CSS_SELECTOR, "div[aria-label='Message Body']"
        send = By.CSS_SELECTOR, "div[class='T-I J-J5-Ji aoO v7 T-I-atl L3']"

        self.driver.find_element(*to).send_keys("shekhu506@gmail.com")
        #sleep(3)
        self.driver.find_element(*subject).send_keys("Test Mail")
        sleep(3)
        self.driver.find_element(*body).send_keys("This mail was generated using selenium")
        sleep(3)
        self.driver.find_element(*send).click()


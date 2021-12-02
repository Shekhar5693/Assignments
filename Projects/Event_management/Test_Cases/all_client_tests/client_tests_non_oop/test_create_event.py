from webdriver_helpers import *

class Test_login_event_creation:
	@pytest.fixture(autouse=True)
	def setup(self,driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)
	
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

#-------------------------------------------------TESTS-----------------------------------------------------------------#
# Test for trying to log in using wrong user name
	def test_login_wrong_username(self, account):
		self.project_site()
		self.client_login()
		assert self.login_wrong_username(account.wrong_username, account.password) == "Invalid username."

# Test for trying to login with wrong password	
	def test_login_wrong_password(self, account):
		self.project_site()
		self.client_login()
		assert self.login_wrong_password(account.username,account.wrong_password) == "Invalid password."

# Test for trying to log in with manager account
	def test_login_using_manager(self,account):
		self.project_site()
		self.client_login()
		assert self.login_manager_account(account.manager_account,account.password) == "Invalid username."

# test for successful logging in and event creation
	@pytest.mark.int
	def test_client_login_event_creation(self, account):
		self.project_site()
		self.client_login()
		self.log_in(account.username, account.password)
		assert self.logged_in() == "Client Dashboard"
		self.fill_event_form(account.username, account.number, account.budget)
		assert self.event_created() == "Event created successfully!"
		self.create_rsvp()
		assert self.rsvp_success() ==  "Thank you!"

# test for creating rsvp
	# def test_rsvp(self, account):
	# 	self.project_site()
	# 	self.client_login()
	# 	self.log_in(account.username, account.password)
	# 	self.create_rsvp()
	# 	assert self.rsvp_success() == "Thank you!"

#-------------------------------------------NAVIGATING TO SITE AND LOGIN PAGE--------------------------------------------#	
	def project_site(self):
		self.driver.get("http://localhost/AD-event-management-main/HomePage/rishabh/")
	
	def client_login(self):
		login_locator = By.PARTIAL_LINK_TEXT, "Login"
		self.driver.find_element(*login_locator).click()
		
		client_locator = By.CSS_SELECTOR, ".ghost[id='signUp']"
		self.wait.until(expected.element_to_be_clickable(client_locator)).click()

		client_login_locator = By.CSS_SELECTOR, "button[formaction='login_client.php']"
		self.wait.until(expected.element_to_be_clickable(client_login_locator)).click()

#-------------------------------------------LOGIN AND EVENT CREATION-----------------------------------------------------#
	def log_in(self, username, password):
		username_locator = By.CSS_SELECTOR, "input[name='username']"
		password_locator = By.CSS_SELECTOR, "input[name='password']"
		submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
		self.driver.find_element(*username_locator).send_keys(username)
		self.driver.find_element(*password_locator).send_keys(password)
		self.driver.find_element(*submit_locator).click()

	def logged_in(self):
		check = By.PARTIAL_LINK_TEXT, "Client Dashboard"
		return self.driver.find_element(*check).text

	def fill_event_form(self, name, number, budget):
		event_button_locator = By.PARTIAL_LINK_TEXT, "Post event"
		self.driver.find_element(*event_button_locator).click()

		name_field_locator = By.CSS_SELECTOR, "input[name='name']"
		self.driver.find_element(*name_field_locator).send_keys(name)

		select_surat = By.CSS_SELECTOR, "[id='floatingSelect'] [value='Surat']"
		self.driver.find_element(*select_surat).click()

		name_field_locator = By.CSS_SELECTOR, "input[name='attendees']"
		self.driver.find_element(*name_field_locator).send_keys(number)
		
		name_field_locator = By.CSS_SELECTOR, "input[name='budget']"
		self.driver.find_element(*name_field_locator).send_keys(budget)

		self.page_down()
		
		venue_names_locator = By.CSS_SELECTOR, "input[type='radio'][name='venue_type']"
		venue_names = self.driver.find_elements(*venue_names_locator)
		venue_names_list = []
		for i in venue_names:
			venue_names_list.append(i.get_attribute("value"))
		venue_name = random.choice(venue_names_list)
		venue_select = By.CSS_SELECTOR, "input[type=radio][value = '{}']".format(venue_name)
		self.driver.find_element(*venue_select).click()

		duration_locator = By.CSS_SELECTOR, "input[name='duration']"
		self.driver.find_element(*duration_locator).send_keys("2")

		date_locator = By.CSS_SELECTOR, "input[name='time']"
		date = self.driver.find_element(*date_locator)
		action:ActionChains = ActionChains(self.driver)
		action.click(date)
		action.send_keys("30112021")
		action.send_keys(Keys.TAB)
		action.send_keys("0630")
		action.send_keys("P")
		action.perform()

		event_locator = By.CSS_SELECTOR, "input[type='radio'][name='event_type']"
		event_names = self.driver.find_elements(*event_locator)
		event_list = []
		for i in event_names:
			event_list.append(i.get_attribute("value"))
		event_name = random.choice(event_list)
		event_select = By.CSS_SELECTOR, "input[type=radio][value = '{}']".format(event_name)
		self.driver.find_element(*event_select).click()

		description_locator = By.CSS_SELECTOR, ".form-control[name='description']"
		self.driver.find_element(*description_locator).send_keys("Need manager for {} celebration.".format(event_name))

		self.page_down()

		submit_locator = By.CSS_SELECTOR, "input[name='submit']"
		self.driver.find_element(*submit_locator).click()

	def event_created(self):
		return self.driver.find_element(By.CSS_SELECTOR,"body > h3:nth-child(3)").text

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

#--------------------------------------------MANAGER ACCOUNT-------------------------------------------------------------#
	def login_manager_account(self,uname,pwd):
		username_locator = By.CSS_SELECTOR, "input[name='username']"
		password_locator = By.CSS_SELECTOR, "input[name='password']"
		submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
		alert = By.CSS_SELECTOR, ".alert"
		self.driver.find_element(*username_locator).send_keys(uname)
		self.driver.find_element(*password_locator).send_keys(pwd)
		self.driver.find_element(*submit_locator).click()		
		return self.driver.find_element(*alert).text

#--------------------------------------------rsvp invite-------------------------------------------------------------#
	def create_rsvp(self):
		rsvp_locator = By.CSS_SELECTOR, "a[href='../RSVP/rsvpHome.html']"
		self.driver.find_element(*rsvp_locator).click()

		sleep(3)

		invite_locator = By.PARTIAL_LINK_TEXT, "Single Invite"
		self.driver.find_element(*invite_locator).click()

		self.driver.switch_to.window(self.driver.window_handles[1])

		name_locator = By.CSS_SELECTOR, "input#name"
		self.driver.find_element(*name_locator).send_keys("Raj")

		yes_locator = By.CSS_SELECTOR, "label[for='Yes']"
		self.driver.find_element(*yes_locator).click()

		cuisine_locator = By.CSS_SELECTOR, "label[for='Italian']"
		self.driver.find_element(*cuisine_locator).click()

		otherCuisine_locator = By.CSS_SELECTOR, "#otherCuisine"
		self.driver.find_element(*otherCuisine_locator).send_keys("N.A.")

		self.driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
		sleep(2)

		specialMessage_locator = By.CSS_SELECTOR, "#specialMsg"
		self.driver.find_element(*specialMessage_locator).send_keys("Congratulations")

		sleep(3)

		submit_locator2 = By.XPATH, "//button[normalize-space()='Submit']"
		self.driver.find_element(*submit_locator2).click()
	
	def rsvp_success(self):
		return self.driver.find_element(By.CSS_SELECTOR, ".alert-heading").text

#-----------------------------------------------------------------------------------------------------------------------#
	def page_down(self):
		html = self.driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
		sleep(1)
		return html

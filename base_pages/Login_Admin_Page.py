from selenium.webdriver.common.by import By



class Login_Admin_Page:
    textbox_username_id = ""
    textbox_password = ""
    btn_login_xpath = ""

#constructor
    def __init__(self, driver):
        self.driver = driver


#action methods
    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password).clear()
        self.driver.find_element(By.ID, self.textbox_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.btn_login_xpath).click()


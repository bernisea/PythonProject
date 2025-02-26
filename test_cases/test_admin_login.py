import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import CustomLogger


class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = CustomLogger.log_generator()

    def test_title_verification(self, setup):

        self.logger.info("****Test_01_Admin_Login title***test_title_verification***")
        self.driver = setup
        #open url
        self.driver.get(self.admin_page_url)
        #actual title
        act_title = self.driver.title
        assert act_title == setup.title
        #This is for verifying the first test connection - exp_title should be modified
        exp_title = "Yahoo | Mail, Weather, Search, Politics, News, Finance, Sports & Videos"
        if act_title == exp_title:
            self.driver.save_screenshot('.\\screenshots\\test_title_verification.png')
            assert True
            self.driver.close()
        else:
            #take screenshot and shot in root folder
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False


    def test_valid_admin_login(self, setup):
        #ARANGE
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)

        #ACT
        self.admin_lp.click_login()

        #ASSERT
        act_dashboard_text = self.driver.find_element(By.XPATH, "locator element").text
        assert act_dashboard_text == "dashboard element"
        self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
        self.driver.close()


    def test_invalid_admin_login(self, setup):
        # ARRANGE
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)

        # ACT
        self.admin_lp.click_login()

        # ASSERT
        error_message = self.driver.find_element(By.XPATH, "page error locator element").text
        assert error_message == "invalid username or password"
        self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
        self.driver.close()

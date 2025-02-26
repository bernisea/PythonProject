import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


#decorate setup
@pytest.fixture()
def setup():
    service = webdriver.ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver
#TODO
#CREAT SETUP(BROWSER) FOR BROWSER OPTIONS



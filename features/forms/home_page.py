import os

from selenium import webdriver
from selenium.webdriver.common.by import By

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "../../browsers/chromedriver")


class HomePage:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_BIN)

    def launch_browser(self):
        pass

    def open_home_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def verify_logo_present(self):
        status = self.driver.find_element(By.XPATH, '//div[@id="divLogo"]//img').is_displayed()
        assert status is True

    def close_browser(self):
        self.driver.close()

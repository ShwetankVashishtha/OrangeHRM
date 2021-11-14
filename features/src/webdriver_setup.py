import os
import unittest
from selenium import webdriver
import urllib3

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "../../browsers/chromedriver")


class WebDriverSetup(unittest.TestCase):
    def set_up(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome(executable_path=DRIVER_BIN)
        self.driver.maximize_window()

    def tear_down(self):
        if self.driver is not None:
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()

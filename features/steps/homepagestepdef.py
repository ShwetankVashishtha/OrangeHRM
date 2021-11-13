import os

from behave import given, when, then
from selenium import webdriver

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "../../drivers/chromedriver")


@given(u'launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=DRIVER_BIN)


@when(u'open orangeHRM home page')
def open_home_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then(u'orangeHRM logo should be present on page')
def verify_logo_present(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True


@then(u'close browser')
def close_browser(context):
    context.driver.close()

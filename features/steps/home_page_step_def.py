from behave import given, when, then
from features.forms.home_page import HomePage

obj_home_page = HomePage()


@given(u'launch chrome browser')
def launch_browser(context):
    obj_home_page.launch_browser()


@when(u'open orangeHRM home page')
def open_home_page(context):
    obj_home_page.open_home_page()


@then(u'orangeHRM logo should be present on page')
def verify_logo_present(context):
    obj_home_page.verify_logo_present()


@then(u'close browser')
def close_browser(context):
    obj_home_page.close_browser()

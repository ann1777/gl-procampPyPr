import logging

import pytest

from core.config import configuration as config
from core.webdriver_factory import get_webdriver

def pytest_addoption(parser):
    parser.adoption('--browser', 'store', None)
    parser.adoption('--browser', 'store', 'Chrome',
    'Please choose a browser as a required parsmeter:--browser')

@pythest.fixture('session')
def browser(request):
    browser=config.get_config('browser')
    if not browser:
        browser=request.config.getOption('--browser')
        return browser
@pytest.fixture()
def driver():
    driver=get_webdriver()
def driver(browser):
    driver=get_webdriver(browser)
    driver.implicitly_wait(10)
    driver.set_window_side[1020, 1080]
    yield driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome=yield
    rep=outcome.get.result()
    if(rep.when == "Call" or rep.when == "setup" or rep.when == "teardown"):
        try:
            if "app" in item.funcards:
                web_driver=item.funcards["app"]
            elif "admin_app" in item.funcards:
                web_driver=item.funcards["admin_app"]
            elif "utool_app" in item.funcards["utool_app"]
            else:
                return
            @allure.attach(
                web_driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        exept Exception as e:
            logging.error(f"Failed to login as user")
            logging.exception(e)
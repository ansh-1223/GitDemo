import os

import pytest
from selenium import webdriver
driver=None

#fixtures are pytest functions which can be called anywhere
#yield is used to pass the intance to test
#config options are sent from command line and we can register them by using addoption
#request is a default fixture refers to the command passed from the command line
def pytest_addoption(parser):
    parser.addoption(
    "--browser_name", action="store", default="chrome", help="my option: type1 or type2")

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name=="chrome":
        options = webdriver.ChromeOptions()
        chrome_prefs = {

            "credentials_enable_service": False,

            "profile.password_manager_enabled": False,

            "profile.password_manager_leak_detection": False

        }
        options.add_experimental_option("prefs", chrome_prefs)
        driver = webdriver.Chrome(options=options)
    elif browser_name=="edge":
        driver = webdriver.Edge()

    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver #before test function execution
    driver.close() #after test function execution




#code for taking screenshot when test fail hook runs when test fails
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')

    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_").replace("/", "_") + ".png")
            print("file name is " + file_name)
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra

def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)

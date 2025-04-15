import os.path
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser: chrome OR firefox OR edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser.lower() == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        options = ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        print("Launching Chrome browser...")
    elif browser.lower() == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
        print("Launching Firefox browser...")
    elif browser.lower() == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        options = EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)
        print("Launching Edge browser...")
    else:
        raise Exception(f"Browser {browser} is not supported.")
    driver.maximize_window()
    return driver

# #It is hook for delete/modify environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%y.html")
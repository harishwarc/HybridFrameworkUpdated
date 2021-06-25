from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#	from selenium import webdriver

@pytest.fixture()

def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        #driver = webdriver.firefox()
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching Firefox browser")
    elif browser == 'edge':
        #driver = webdriver.edge()
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


###Pytest HTML report

def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop commerce Demo Testing'
    config._metadata['Module name'] = 'Customers'
    config._metadata['Tester'] = 'Harishwar'

@pytest.mark.optionalhook

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)
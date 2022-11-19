from msedge.selenium_tools import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GecoDriverManager, GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.utils import ChromeType

from core.settings import BROWSER

def get_driver(BROWSER=None):
    '''Get webdriver according to BROWSER'''
    driver = None
    if BROWSER == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager(ChromeType.CHROMIUM).install())
    elif BROWSER == 'firefox':
        driver = webdriver.Firefox(GecoDriverManager().install())
    elif BROWSER == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif BROWSER == 'opera':
        driver = webdriver.Opera(OperaDriverManager().install())
    return driver

def get_browsers_dict(requested_driver: str):
    browsers_dict = {
        'chrome': __get_chrome(),
        'firefox': __get_firefox(),
        'edge': __get_edge(),
        'opera': __get_opera()
       }
    try:
        return browsers_dict[requested_driver]()
    except ValueError:
        raise Exception ('Browser is not supported')

def __get_chrome():
    options=webdriver.ChromeOptions()
    chrome_driver=webdriver.Chrome(ChromeDriverManager().install(), options)
    return chrome_driver

def __get_firefox():
    options=webdriver.FirefoxOptions()
    firefox_driver=webdriver.Firefox(GeckoDriverManager().install(), options)
    return firefox_driver

def __get_edge():
    capabilities=webdriver.DesiredCapabilities().EDGE
    edge_driver=webdriver.Edge(EdgeChromiumDriverManager().install(), capabilities)
    return edge_driver

def __get_opera():
    opera_driver=webdriver.Opera(OperaDriverManager().install())
    return opera_driver

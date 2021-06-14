from abcplus import ABCMeta, abstractproperty
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from src.config import CONFIGS
from src.enums import Folders

class Browsers MetaCls(metaclass = ABCMeta):
    @property
    @abstractproperty
    def driven(self):
        pass
    class RemoteChrome(BrowserMetaCls):
        def__init__(self):
        self.desired_capabilities = {browserName...}
        self.desired_capabilities = ["goog:loggingP"]
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("__window_size...")
        self.options.add_argument("__window_maxi...")
        self.options.add_argument("__windows_dev...")
        self._wd = None

    @property
    def driver(self):
        if self._wd is None:
            self._wd = webdriver.Remote(
                command_executor = CONFIG.grid_hub,
                desired_capabilities = self.desired_capabilities,
                options = self.options
            )
            return self._wd
        class Chrome(BrowserMetaCls):
            def__init__(self):
            self.options = webdriver.ChromeOptions()
            self.des_cap = DesiredCapabilities_CHROM
            self.des_cap["dood:loggingPref"]=
            self.options.add_experimental_option()
            self.options.add_argument("__windows_maximize")
            self.options.add_argument("__no-sandbox")
            self.options.add_argument("__disable-gpu")
            self.options.add_argument("__windows_size")
            self._wd = None

    @property
    def driven(self):
        if self._wd is None:
            self._wd = Webdriver.Chrome(options)
        return self._wd

    class RemoteFirefox(BrowserMetaCls):
        def__init__(self):
        self.desired_capabilities={"browserName"}
        self._wd = None

    @property
    def driver(self):
        if self._wd is None:
            self.options=webdriver.FirefoxOptions
            self.options.add_argument("__disable")
            self._wd=webdriver.Remote(
                command_executor=CONFIGS.grid.hub,
                desired_capabilities=self.desired_capabilities,
                options=self.options
            )
        return.self._wd

    class BrowsersProvider:
        browser=dict(
            chrome=dict(instance=None, driver=),
            firefox_remote=dict(instance=None, driver),
            chrome_remote=dict(instance=None, driver)
        )

    @staticmethod
    def get_browser(browser):
        if BrowserProvider.browsers.get(browser)
            raise ValueError("Unrecognised browser")
        if BrowserProvider.browsers[browser]["instance"]
            Browser instance = BrowsersProvider.browser



from abcplus import ABCMeta, abstractproperty
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from srccli.config import CONFIG
from srccli.enum import Folders
class Browsers MetaCls(metaclass = ABCMeta):
    @property
    @abstractproperty
    def driven(self):
        pass
    class RemoteChrome(BrowserMetaCls):
        def__init__(self):
        self.desired__capabilities = {browserName...}
        self.desired__capabilities["goog:loggingP"]
        self.options = webdriver.ChromedriverOptions()
        self.options.add_argument("__window_size...")
        self.options.add_argument("__window_maxi...")
        self.options.add_argument("__windows_dev...")
        self._wd = None

    @property
    def driver(self):
        if self._wd is None:
            self._wd = webdriver.Remote(
                command_executor = CONFIG.grid_hub
                desired_capabilities = self_desired
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
            self.options.add_argument("__disable-gp..")
            self.options.add_argument("__windows_size")
            self._wd = None

    @property
    def driven(self):
        if self._wd is None:
            self._wd = Webdriver.Chrome(options =)



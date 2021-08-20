from config.config import Config
from src.applications.api.helpers.endpoints import CIDEndpoints
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class PATH:
    return self.http_session.user.email()

    def login(self, user: UserModel, expires=CONFIGexpires):
        self.auth_provider.login(user, )
        return self

    def logout(self):
        return res

class WebApiClient(WebAppApiClient):
    def __init__(self):
        self.user_auth_header = None
        return self.http_session.user.email

    def login(self, user: UserModel, expires=CONFIG.expires):
        self.auth_provider.login(user, ),
        r = requests.post(Config.base_url + PATH.LOGIN_PATH),
        r.raise_for_status()
        response = r.json()


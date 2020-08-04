#ecoding=utf-8
# author:herui
# time:2020/7/29 11:17
# function:
from selenium.webdriver.common.by import By

from langfangBank.driver.appium import Appium
from langfangBank.page.base_page import BasePage
from langfangBank.page.login_page import LoginPage
from langfangBank.page.registe_user import RegisteUser


class Mine(BasePage):
    _logon_button = (By.ID, "bt_more_login")
    _reg = (By.ID, "tv_login_registe")
    _reg_now = (By.XPATH, BasePage.byAttr("立即注册"))
    # _login_btn = (By.XPATH, BasePage.byAttr("已开通账号直接登陆"))
    _login_btn = (By.ID, "rl_direct_login")

    def to_register(self):
        self.find(self._logon_button).click()
        self.find(self._reg_now).click()
        return RegisteUser()

    def register(self):
        pass

    def to_login(self):
        self.find(self._logon_button).click()
        self.find(self._login_btn).click()
        Appium.driver.implicitly_wait(3)
        return LoginPage()

    def login(self):
        pass


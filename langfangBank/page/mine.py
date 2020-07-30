#ecoding=utf-8
# author:herui
# time:2020/7/29 11:17
# function:
from selenium.webdriver.common.by import By

from langfangBank.page.base_page import BasePage
from langfangBank.page.registe_user import RegisteUser


class Mine(BasePage):
    _logon_button = (By.ID, "bt_more_login")
    _reg = (By.ID, "tv_login_registe")
    _reg_now = (By.XPATH, BasePage.byAttr("立即注册"))

    def to_register(self):
        self.find(self._logon_button).click()
        self.find(self._reg_now).click()
        return RegisteUser()

    def register(self):
        pass

    def to_login(self):
        pass

    def login(self):
        pass


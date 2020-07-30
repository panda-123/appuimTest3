#ecoding=utf-8
# author:herui
# time:2020/7/29 10:42
# function:
from selenium.webdriver.common.by import By

from langfangBank.page.base_page import BasePage
from langfangBank.page.mine import Mine


class HomePage(BasePage):

    _mine = (By.XPATH, BasePage.byAttr(text="我的", id='rb_more'))
    _home_page = (By.XPATH, BasePage.byAttr(text="首页"))
    _all_server = (By.XPATH, BasePage.byAttr(text="全部服务"))
    _loan = (By.XPATH, BasePage.byAttr(text="贷款"))

    def to_mine(self):
        self.find(self._mine).click()
        return Mine()

    def to_homepage(self):
        self.find(self._home_page).click()
        return self

    def to_all_server(self):
        self.find(self._all_server).click()
        return self

    def to_loan(self):
        self.find(self._loan).click()
        return self

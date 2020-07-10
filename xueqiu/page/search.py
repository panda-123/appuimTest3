#ecoding=utf-8
# author:herui
# time:2020/7/7 17:18
# function:
from selenium.webdriver.common.by import By
from xueqiu.page.BasePage import BasePage
from xueqiu.driver.Appium import Appium


class Search(BasePage):
    _search=(By.ID,"search_input_text")
    _name = (By.ID, "name")
    _usr = (By.XPATH, "//*[@text='用户']")
    _usrName = (By.ID, "user_name")
    def search(self,keyword):
        self.find(*self._search).send_keys(keyword)
        return self
    def getStocks(self):
        return self.find(*self._name).text

    def getUserName(self):
        self.find(*self._usr).click()
        return self.find(*self._usrName).text
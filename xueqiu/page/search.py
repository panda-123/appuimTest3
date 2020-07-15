#ecoding=utf-8
# author:herui
# time:2020/7/7 17:18
# function: 实现搜索功能
from selenium.webdriver.common.by import By
from xueqiu.page.base_page import BasePage
from xueqiu.driver.Appium import Appium
from xueqiu.page.portfolio import Portfolio


class Search(BasePage):
    _search=(By.ID,"search_input_text")
    _name = (By.ID, "name")
    _usr = (By.XPATH, "//*[@text='用户']")
    _usrName = (By.ID, "user_name")
    _portfolio = (By.XPATH,"//*[@text='行情' and contains(@resource-id, 'tab_name')]")
    def search(self,keyword):
        self.find(self._search).send_keys(keyword)
        return self

    def getStocks(self):
        return self.find(self._name).text

    def toNextPage(self):
        # 从搜索页面跳转至显示用户页签的页面
        self.find(self._name).click()
        return self

    def getUserName(self):
        # 去用户页面
        self.find(self._usr).click()
        return self.find(self._usrName).text

    def toPortfolio(self):
        self.find(self._portfolio).click()
        return Portfolio()

    def loaded(self):
        locations = ["x", "y"]
        while locations[-1] != locations[-2]:
            element = self.find(self._portfolio)
            print(element)
            locations.append(element.location)
            print(locations)

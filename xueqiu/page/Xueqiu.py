#ecoding=utf-8
# author:herui
# time:2020/7/7 16:04
# function:
from selenium.webdriver.common.by import By

from xueqiu.driver.Appium import Appium
from xueqiu.page.BasePage import BasePage
from xueqiu.page.search import Search


class XueQiu(BasePage):
    _homeSearch = (By.ID, "home_search")
    def toSearch(self):
        self.find(*self._homeSearch).click()
        return Search()

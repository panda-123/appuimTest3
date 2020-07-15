#ecoding=utf-8
# author:herui
# time:2020/7/15 15:32
# function: 实现自选功能
from selenium.webdriver.common.by import By

from xueqiu.page.base_page import BasePage
from xueqiu.page.search import Search

class Portfolio(BasePage):
    _search_button = (By.ID, "action_create_cube")
    def toSearch(self):
        self.find(self._search_button).click()
        return Search()
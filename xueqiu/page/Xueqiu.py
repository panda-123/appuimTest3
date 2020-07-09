#ecoding=utf-8
# author:herui
# time:2020/7/7 16:04
# function:

from xueqiu.driver.Appium import Appium
from xueqiu.page.search import Search


class XueQiu(object):
    def toSearch(self):
        Appium.driver.find_element_by_id("home_search").click()
        return Search()

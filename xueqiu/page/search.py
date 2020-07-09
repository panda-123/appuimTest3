#ecoding=utf-8
# author:herui
# time:2020/7/7 17:18
# function:
from xueqiu.driver.Appium import Appium


class Search(object):
    def search(self,keyword):
        Appium.driver.find_element_by_id("search_input_text").send_keys(keyword)
        return self
    def getStocks(self):
        return Appium.driver.find_element_by_id("name").text

    def getUserName(self):
        Appium.driver.find_element_by_xpath("//*[@text='用户']").click()
        return Appium.driver.find_element_by_id("user_name").text
#ecoding=utf-8
# author:herui
# time:2020/6/8 18:16
# function:

from appium import webdriver

class Find_Element():
    def __init__(self):
        self.driver =  webdriver.Remote()

    def by_xpath(self,text,resource_id):
        element = self.driver.find_element_by_xpath(
            "//*[@text=text and contains(@resource-id, resource_id)]")
        return element
    def by_id(self,id):
        element = self.driver.find_element_by_id(id)
        return element
    def by_name(self):
        pass
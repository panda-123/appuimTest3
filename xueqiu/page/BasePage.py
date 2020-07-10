#ecoding=utf-8
# author:herui
# time:2020/7/6 11:25
# function:
from selenium.webdriver.common.by import By

from xueqiu.driver.Appium import Appium
from lxml import etree

class BasePage(object):
    # 黑名单，处理随时可能的弹窗
    blank_words = ["//*[text='好的']"]
    def findBy(self,by=By.ID, value = None):
        try:
            return Appium.driver.find_element(by, value)
        except:
            page_source = Appium.driver.page_source
            print(page_source)
            xml = etree.XML(page_source)
            for w in self.blank_words:
                print(w)
                if(len(xml.xpath(w))>0):
                    Appium.driver.find_element(By.XPATH, w).click()

    def find(self,by,value):
        try:
            return Appium.driver.find_element(by,value)
        except:
            page_source = Appium.driver.page_source
            print(page_source)
            xml = etree.XML(page_source)
            for w in self.blank_words:
                print(w)
                if(len(xml.xpath(w))>0):
                    Appium.driver.find_element(By.XPATH, w).click()

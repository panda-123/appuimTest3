#ecoding=utf-8
# author:herui
# time:2020/7/15 15:48
# function:股票页面功能
from selenium.webdriver.common.by import By

from xueqiu.page.portfolio import Portfolio

class Stock(Portfolio):
    _name = (By.ID, "com.xueqiu.android:id/portfolio_stockName")
    _us = (By.XPATH,"//*[@text='美股']")
    def getNameByUS(self):
        self.find(self._us).click()
        x=[]
        for e in self.findAll(self._name):
            x.append(e.text)
        return x

    def getByGroup(self):
        pass
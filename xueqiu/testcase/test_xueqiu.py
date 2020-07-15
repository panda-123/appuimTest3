#ecoding=utf-8
# author:herui
# time:2020/7/7 15:29
# function:

import unittest
from xueqiu.driver.Appium import Appium
from xueqiu.page import xueqiu

class test_XueQiu(unittest.TestCase):

    def setUp(self):
        Appium.initDriver()
        # print(Appium.initDriver())

    def test_search(self):
        assert xueqiu.XueQiu().toSearch().search("pdd").getStocks() == "拼多多"

    def test_search_UserName(self):
        # 判断用户中第一个人的姓名是不是叫 seveniruby
        xueqiu2 = xueqiu.XueQiu()
        searchpage = xueqiu2.toSearch()
        searchpage.search("seveniruby").toNextPage()
        assert searchpage.getUserName() >= "seveniruby"



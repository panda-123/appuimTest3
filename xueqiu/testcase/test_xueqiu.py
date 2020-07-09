#ecoding=utf-8
# author:herui
# time:2020/7/7 15:29
# function:

import unittest
from xueqiu.driver.Appium import Appium
from xueqiu.page import Xueqiu

class test_XueQiu(unittest.TestCase):

    def setUp(self):
        Appium.initDriver()
        # print(Appium.initDriver())

    def test_search(self):
        assert Xueqiu.XueQiu().toSearch().search("pdd").getStocks() == "拼多多"

    def test_search_UserName(self):
        xueqiu = Xueqiu.XueQiu()
        searchpage = xueqiu.toSearch()
        searchpage.search("herui")
        assert searchpage.getUserName() == "herui"



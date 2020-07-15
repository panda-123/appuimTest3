#ecoding=utf-8
# author:herui
# time:2020/7/15 16:21
# function:
import unittest
import pytest

from xueqiu.page.stock import Stock
from xueqiu.page.xueqiu import XueQiu
from xueqiu.driver.Appium import Appium
from xueqiu.page.search import Search

class test_Portfolio(unittest.TestCase):
    def setUp(self) -> None:
        Appium.initDriver()
        self.stock = Search.toPortfolio()
    def test_list(self):
        print( Stock.getNameByUS())
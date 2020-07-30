#ecoding=utf-8
# author:herui
# time:2020/7/29 11:21
# function:
import unittest
import pytest

from langfangBank.driver.appium import Appium
from langfangBank.page.home_page import HomePage


class TestLogin(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        # todo:数据初始化
        Appium.initDriver()
        cls.home = HomePage()
        cls.reg = cls.home.to_mine().to_register()

    def test_reg(self):
        ID = "310105198812215979"
        name = "张佳刚"
        CardNo = "6221409000649437"
        name2 = "zhangjiagang"
        pwd2 = "ll1111"
        phoneNum = "15132728166"
        self.reg.authentication(ID, name).reg_info(CardNo,name2,pwd2).sec_question(phoneNum)
        assert self.reg.get_reg_result() == "注册成功"


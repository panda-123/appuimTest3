# ecoding=utf-8
# author:herui
# time:2020/7/29 11:21
# function:
import unittest
import pytest

from langfangBank.driver.appium import Appium
from langfangBank.page.home_page import HomePage


class TestLogin(object):

    @classmethod
    def setup_class(cls):
        # todo:数据初始化
        Appium.initDriver()
        cls.home = HomePage()
        cls.mine = cls.home.to_mine()
        # cls.reg = cls.mine.to_register()
        # cls.log = cls.home.to_mine().to_login()

    @pytest.mark.parametrize("ID,name,CardNo,name2,pwd2,phoneNum",
                [("440903196907191800","连阳桂","6221409000649429","lianyanggui","ll1111","18293646022"),
                 ("350400195112041697","谷莉芝","6221409000649411","gulizhi","ll1111","18323204657"),
                 ("510421195606265094","夏淑","6221409000649403","xiashu","ll1111","15621058020")])
    def test_reg(self,ID,name,CardNo,name2,pwd2,phoneNum):
        self.mine.to_register().authentication(ID, name).reg_info(CardNo,name2,pwd2).sec_question(phoneNum)
        assert self.mine.to_register().get_reg_result() == "注册成功"

    @pytest.mark.parametrize("usrName,pwd",[("lianyanggui","111111")])
    def test_login(self,usrName,pwd):
        self.mine.to_login().input_info(usrName,pwd)


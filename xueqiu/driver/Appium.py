#ecoding=utf-8
# author:herui
# time:2020/7/3 17:30
# function:

from appium import webdriver
import pytest
import unittest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import os

class Appium(object):
    driver = None
    "@type driver: WebDriver"

    def setUp(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "MIMax"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 设置不清除已有数据
        caps["noReset"] = "True"
        caps["fullReset"] = "False"
        # 从底层获取一些权限，规避获取权限的弹框
        caps["autoGrantPermissions"] = "true"
        # remote方法:远程连接命令行工具
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

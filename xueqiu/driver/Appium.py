#ecoding=utf-8
# author:herui
# time:2020/7/3 17:30
# function:

from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class Appium(object):

    driver = None
    "@type driver: WebDriver"
    # 下面方法适用于python 3.5以上
    # driver: WebDriver = None

    @classmethod
    def getDriver(cls):
        return cls.driver
    @classmethod
    def initDriver(cls):
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
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

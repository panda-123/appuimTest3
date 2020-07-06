#ecoding=utf-8
# author:herui
# time:2020/5/18 14:45
# function:

from appium import webdriver
import pytest
import unittest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import os

# 采用unittest风格，使用pytest运行

class test_XueQiu(unittest.TestCase):
    def setUp(self):
        print("setup")
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

    def find(self,by,locator):
        # 通过异常处理+黑名单列表，处理随时可能出现的弹窗
        # 这里为伪代码，先提供思路
        try:
            self.driver.find_element(by, locator)
        except:
            keywords = []
            for key in keywords:
                elements=self.driver.find_elements(key)
                if len(elements)>0:
                    elements[0].click()

    def test_search(self):
        self.driver.find_element_by_id("tv_agree").click()
        self.driver.find_element_by_id("image_cancel").click()
        self.driver.find_element_by_id("home_search").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("search_input_text").send_keys("JD")
        self.driver.implicitly_wait(5)
        # 隐式等待，等5秒后再进行下一步操作
        self.driver.find_element_by_xpath("//*[@text='京东']").click()
        assert self.driver.find_element_by_id("name").text == "京东"

    def test_check_stock(self):
        for i in range(1, 5):
            element = self.driver.find_element_by_xpath(
                "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
            print(element.location)
            element.get_attribute("text")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        assert 1 == len(self.driver.find_elements_by_xpath(
            "//*[contains(@resource-id, 'portfolio_stockName') and @text='京东']"))

    def test_touch(self):
        el1 = self.driver.find_element_by_id("")
        el2 = self.driver.find_element_by_id("")
        self.driver.get_window_size()
        action = TouchAction(self.driver)
        action.move_to(el1,el2)
        action.press()
        pass

    def swipe(self):
        mob_size = self.driver.get_window_size()
        x = mob_size['width']
        y = mob_size['height']
        print(x, y)
        x_init = x * 0.5
        y_init = y * 0.5
        x_start = x * 0.10
        x_end = x * 0.90
        y_start = y * 0.10
        y_end = y * 0.90
        # size_set = {"x_start":x * 0.25,"x_end":x*0.90,"y_start":y * 0.25,"y_end":y * 0.90}
        director = ["up","down","right","left"]
        # element = self.driver.find_element_by_xpath("//*[@text='雪球热股']")
        for i in director:
            if i == "up":
                self.driver.swipe(x_init, y_end, x_init, y_start)
                print("up--up--------------")
                sleep(1)
            elif i == "down":
                self.driver.swipe(x_init, y_start, x_init, y_end)
                print("down--down--------------")
                sleep(1)
            elif i == "left":
                self.driver.swipe(x_end, y_init, x_start, y_init)
                print("left--left--------------")
                sleep(1)
            elif i == "right":
                self.driver.swipe(x_start, y_init, x_end, y_init)
                print("right----------------")
                sleep(1)
        # return element

    def test_run_swipe(self):
        sleep(10)
        print(self.swipe())


    def test_swipe(self,by,director):
        mob_size = self.driver.get_window_size()
        x = mob_size['width']
        y = mob_size['height']
        print(x, y)
        if director == "up":
            x_start = x*0.5
            y_start = y*0.25
            y_end = y*0.75
            self.driver.swipe(x_start,y_start,x_start,y_end)
        elif director == "down":
            x_start = x*0.5
            y_start = y*0.75
            y_end = y*0.25
            self.driver.swipe(x_start,y_start,x_start,y_end)
        elif director == "left":
            x_start = x*0.75
            y_start = y*0.5
            x_end = y*0.25
            self.driver.swipe(x_start,y_start,x_end,y_start)
        elif director == "right":
            x_start = x*0.25
            y_start = y*0.5
            x_end = y*0.75
            self.driver.swipe(x_start,y_start,x_end,y_start)



    def test_get_size(self):
        # return element
        mob_size = self.driver.get_window_size()
        print(type(mob_size))
        print(mob_size)
        x = mob_size['width']
        y = mob_size['height']
        print(x,y)

    def close_Popups(self):
        self.driver.find_element_by_id("tv_agree").click()
        self.driver.find_element_by_id("image_cancel").click()

    def loaded(self):
        # 处理有加载，页面不稳定的情况
        locations = ["x","y"]
        while locations[-1] != locations[-2]:
            element = self.driver.find_element_by_xpath(
                "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
            locations.append(element.location)
            print(locations)

    def test_webView_sim_image(self):
        # self.loaded()
        # self.close_Popups()
        self.driver.find_element_by_xpath("//*[@text='交易']").click()
        # for i in range(6):
        #     sleep(3)
        #     print(self.driver.page_source)
        #     print()
        # 图片的content-desc：16e172ee2be2a473fee98fc7
        self.driver.find_element_by_accessibility_id("16e172ee2be2a473fee98fc7").click()

    def test_webView_sim_h5(self):
        # 运行报错，没有合适的chromedriver
        sleep(2)
        self.driver.find_element_by_xpath("//*[@text='交易']").click()
        for i in range(2):
            sleep(2)
            print(self.driver.contexts)
            print(self.driver.current_context)
            print(self.driver.page_source)
            print()
        # switch_to 切换上下文
        self.driver.switch_to.context("WEBVIEW_com.xueqiu.android")
        print(self.driver.current_context)
        print(self.driver.page_source)

    def test_battery(self):
        print("手机电量：")
        print(self.driver.execute_script('mobile:batteryInfo'))

    def test_shell(self):
        print(self.driver.execute_script("mobile:shell",
                                         {"command":"am",
                                          "args":["start","-n","com.android.calcultor2/.Calculator"]}),
              )

    # tearDown清理环境
    def tearDown(self):
        sleep(10)
        self.driver.quit()








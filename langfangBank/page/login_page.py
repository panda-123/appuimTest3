#ecoding=utf-8
# author:herui
# time:2020/8/3 18:01
# function:
from selenium.webdriver.common.by import By

from langfangBank.driver.appium import Appium
from langfangBank.page.base_page import BasePage

import time

class LoginPage(BasePage):
    _usr_name = (By.ID, "et_name")
    _usr_pwd = (By.ID, "pge_loginpwd")
    _login_bt = (By.ID, "bt_login")


    def input_info(self,usrName,pwd):
        """
        step1:输入用户名
        step2:找到密码输入，调出安全键盘，点击输入密码
        """
        #todo:优化密码输入，明文输入不识别
        self.find(self._usr_name).send_keys(usrName)
        self.find(self._usr_pwd).click()
        try:
            Appium.driver.save_screenshot("../screen/pwd.png")
            self.click_pwd(pwd)
        except:
            time.sleep(5)
        self.find(self._login_bt).click()
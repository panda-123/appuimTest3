#ecoding=utf-8
# author:herui
# time:2020/7/29 15:28
# function:
import time

from selenium.webdriver.common.by import By

from langfangBank.page.base_page import BasePage


class RegisteUser(BasePage):

    _id_card = (By.ID, "et_id_card")
    _name = (By.ID, "et_name")
    _agree_selector = (By.ID, "cb_agree")
    _bt_next = (By.ID, "bt_next")
    _Card_No = (By.ID, "et_cardNO")
    _Card_pwd = (By.ID, "pge_password_regist")
    _set_name = (By.ID, "et_loginname")
    _set_pwd = (By.ID, "pge_loginpwd_regist")
    _config_pwd = (By.ID, "pge_confirmPwd")
    _input_ans = (By.XPATH, BasePage.byAttr("请输入答案"))
    _phone_num = (By.XPATH, BasePage.byAttr("请输入手机号码"))
    _get_code = (By.XPATH, BasePage.byAttr("获取验证码"))
    # _input_code = (By.XPATH, BasePage.byAttr("请输入验证码"))
    _input_code = (By.ID, "et_mobileVerCode")
    _ok_btn = (By.ID, "bt_ok")
    _result = (By.XPATH, BasePage.byAttr("注册成功"))

    def authentication(self, ID, Name):
        self.find(self._id_card).send_keys(ID)
        self.find(self._name).send_keys(Name)
        self.find(self._agree_selector).click()
        self.find(self._bt_next).click()
        return self

    def reg_info(self, CardNo, name, pwd2, pwd=""):
        #todo:手动输入密码
        self.find(self._Card_No).send_keys(CardNo)
        self.find(self._Card_pwd).send_keys(pwd)
        time.sleep(10)
        self.find(self._set_name).send_keys(name)
        self.find(self._set_pwd).send_keys(pwd2)
        time.sleep(10)
        self.find(self._config_pwd).send_keys(pwd2)
        time.sleep(10)
        self.find(self._bt_next).click()
        return self

    def sec_question(self,phoneNum,code="123456"):
        elements= self.findAll(self._input_ans)
        if len(elements)>=1:
            elements[0].send_keys("爷爷")
            elements[1].send_keys("班主任")
            elements[2].send_keys("1001")
        self.find(self._phone_num).send_keys(phoneNum)
        self.find(self._get_code).click()
        time.sleep(3)
        self.find(self._input_code).send_keys(code)
        time.sleep(5)
        self.find(self._ok_btn).click()

    def get_reg_result(self):
        return self.find(self._result).text


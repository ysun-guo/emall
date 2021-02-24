# coding:utf-8

from public.BasePage import BasePage
from selenium.webdriver.common.by import By
from public.readConf import ReadConf
import requests
import datetime
from selenium.webdriver.support import expected_conditions as ec
import logging


class LoginPage(BasePage):

    _phone = (
        By.XPATH,
        "//uni-view[@class='form-input-group'][1]/uni-input/div/input")
    _pwd = (
        By.XPATH,
        "//uni-view[@class='form-input-group'][2]/uni-input/div/input")
    _get_code_btn = (By.CLASS_NAME, "get-code")
    _submit_btn = (By.CLASS_NAME, "can-submit-btn")
    _invite_cancel = (By.CLASS_NAME, "invite-code-cancel")

    def find_phone_ele(self):
        return self.find_element(self._phone)

    def send_phone(self):
        phone = ReadConf().readconf("PhoneNumber", "phone")
        self.sendkey_element(self.find_phone_ele(), phone)

    def click_get_code_btn(self):
        self.click_element(self._get_code_btn)
        req_time = datetime.datetime.now()
        return req_time

    def find_pwd_ele(self):
        return self.find_element(self._pwd)

    def send_pwd(self, code):
        self.sendkey_element(self.find_pwd_ele(), code)

    def click_submit_btn(self):
        self.click_element(self._submit_btn)

    def click_invite_cancel(self):
        if BasePage(self.driver).is_element_present(self._invite_cancel):
            self.click_element(self._invite_cancel)
        else:
            print("没有出现输入邀请码页面")

    @staticmethod
    def get_code_by_api(saas_token, req_time):
        host = ReadConf().readconf("HOST", "admin_host")
        tenant_id = ReadConf().readconf("Tenant", "tenant_id")
        phone = ReadConf().readconf("PhoneNumber", "phone")
        start_time = datetime.datetime.strftime((req_time + datetime.timedelta(minutes=-1)), '%Y-%m-%d %H:%M:%S')
        end_time = datetime.datetime.strftime(req_time, '%Y-%m-%d %H:%M:%S')
        api = '/api/v1/statistics/sms/list'
        url = host + api
        header = {
            "token": saas_token,
            "tenantId": tenant_id
        }
        body = {
            "state": 1,
            "notifyTarget": phone,
            "startIndex": 0,
            "pageCount": 20,
            "startCreated": start_time,
            "endCreated": end_time,
            "notifyCode": "vcode"
        }
        text = requests.get(url, headers=header, params=body)
        x = text.json()["body"]["data"]
        code = None
        for i in x:
            code = i["content"][6:12]
            break
        return code

    def get_code(self, saas_token, req_time):
        code = self.get_code_by_api(saas_token, req_time)
        logging.info(code)
        start_time = datetime.datetime.utcnow()
        while True:
            end_time = datetime.datetime.utcnow()
            tc = end_time - start_time
            if code is None and tc.seconds < 30:
                code = self.get_code_by_api(saas_token, req_time)
            else:
                break
        return code

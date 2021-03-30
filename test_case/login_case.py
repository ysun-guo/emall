# coding:utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from pages.login_page import LoginPage
from public.readConf import ReadConf
from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import logging
from selenium.common import exceptions
import os
from unittest import TestCase
import datetime


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        return_list = BasePage(cls).class_setup_set(False)
        cls.driver = return_list[0]
        cls.token = return_list[1]

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url(ReadConf().readconf("URL", "cartURL"))

    def test_login_success(self):
        '''
        手机号、验证码成功登陆
        '''
        logging.info('**输入正确的手机号、验证码，点击登录，验证登录成功**')
        admin_token = LoginPage(self.driver).return_saas_token_by_api()
        LoginPage(self.driver).send_phone()
        start_time = LoginPage(self.driver).click_get_code_btn()
        logging.info(start_time)
        code = LoginPage(self).get_code(admin_token, start_time)
        get_code_time = datetime.datetime.now()
        logging.info(get_code_time)
        if code is not None:
            LoginPage(self.driver).send_pwd(code)
            LoginPage(self.driver).click_submit_btn()
            sleep(2)
            try:
                LoginPage(self.driver).click_invite_cancel()
            except exceptions.TimeoutException:
                logging.info('**m没有出现输入邀请码页面**')
            logging.info(self.driver.current_url)
            current_url = self.driver.current_url
            BasePage(self.driver).assert_true('login/hLogin' not in current_url)
            BasePage(self.driver).assert_true(BasePage(self.driver).is_element_present((By.CLASS_NAME, "uni-tabbar")))
            BasePage(self.driver).check_exist_in_page("购物车")
            sleep(2)
        else:
            TestCase().fail(msg="没有收到验证码")


if __name__ == '__main__':
    unittest.main()

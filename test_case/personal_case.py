# coding=utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from pages.personal_page import PersonalPage
import logging
import os
from public.readConf import ReadConf
from selenium.webdriver.support import expected_conditions as ec
from ddt import *
from unittest import TestCase


@ddt
class CategoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver_path = os.getcwd() + '/chromedriver'
        # driver_path = 'chromedriver'
        options = BasePage(cls).device_dev_set()
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
        cls.driver.implicitly_wait(5)
        BasePage(cls.driver).visit_url()
        BasePage(cls.driver).login_by_js(True)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url(ReadConf().readconf("URL", "personalURL"))

    def test_page_show_check(self):
        logging.info('**验证我的页面的元素是否已经展示**')
        res = BasePage(self.driver).is_element_present(PersonalPage(self.driver)._order)
        if res is True:
            logging.info('订单模块显示在页面上')
        else:
            TestCase().fail('页面中未找到订单模块')
        BasePage(self.driver).assert_true(
            BasePage(self.driver).is_element_present(PersonalPage(self.driver)._distribution))
        BasePage(self.driver).assert_true(
            BasePage(self.driver).is_element_present(PersonalPage(self.driver)._member_info))
        BasePage(self.driver).assert_true(
            BasePage(self.driver).is_element_present(PersonalPage(self.driver)._other_item))
        BasePage(self.driver).assert_true(
            BasePage(self.driver).is_element_present(PersonalPage(self.driver)._saas_link))
        BasePage(self.driver).check_exist_in_string('我的', self.driver.title)


if __name__ == '__main__':
    unittest.main()

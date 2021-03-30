# coding=utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from pages.home_page import HomePage
import logging
import os
from unittest import TestCase


class HomeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        return_list = BasePage(cls).class_setup_set(True)
        cls.driver = return_list[0]
        cls.token = return_list[1]

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url()

    def test_home_check(self):
        '''
        首页的元素检查
        '''
        logging.info('**验证首页的橱窗、广告模板等是否已经展示**')
        res = BasePage(self.driver).is_element_present(HomePage(self.driver)._banner)
        if res is True:
            logging.info('banner已展示')
        else:
            TestCase().fail('banner未展示')
        res = BasePage(self.driver).is_element_present(HomePage(self.driver)._product)
        if res is True:
            logging.info('product已展示')
        else:
            TestCase().fail('product未展示')
        res = BasePage(self.driver).is_element_present(HomePage(self.driver)._advert)
        if res is True:
            logging.info('广告位已展示')
        else:
            TestCase().fail('广告位未展示')
        res = BasePage(self.driver).is_element_present(HomePage(self.driver)._shopWindow)
        if res is True:
            logging.info('橱窗已展示')
        else:
            TestCase().fail('橱窗未展示')
        res = BasePage(self.driver).is_element_present(HomePage(self.driver)._search_box)
        if res is True:
            logging.info('搜索框已展示')
        else:
            TestCase().fail('搜索框未展示')

    def test_goto_saas(self):
        '''
        跳转到saas页面
        '''
        HomePage(self.driver).click_saas_link_img()
        res = BasePage(self.driver).is_element_present(HomePage(self.driver)._saas_personal_info)
        if res is True:
            logging.info('saas的个人信息页面已展示')
        else:
            TestCase().fail('saas页面个人信息模块未展示')
        BasePage(self.driver).check_exist_in_string('saash5', BasePage(self.driver).get_url())


if __name__ == '__main__':
    unittest.main()

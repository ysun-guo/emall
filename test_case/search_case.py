# coding=utf-8
import unittest
from ddt import *
from public.BasePage import BasePage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from time import sleep

import os


@ddt
class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        return_list = BasePage(cls).class_setup_set(False)
        cls.driver = return_list[0]
        cls.token = return_list[1]

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url()

    @data("优惠金额验证")
    def test_search(self, value):
        '''
        输入商品名称进行搜索
        '''
        print('**输入商品名称搜索，验证是否有搜索到相关商品**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box(value)
        sleep(2)
        for productName in SearchPage(self.driver).get_product_names():
            name = SearchPage(self.driver).get_element_value(productName)
            print("商品名称:" + name)
            BasePage(self.driver).check_exist_in_string(value, name)

    def test_search_cancel(self):
        '''
        在搜索页，点击取消按钮，返回到上一页
        '''
        print('**在搜索页面点击取消，验证是否会返回到首页**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).click_cancel_button()
        sleep(2)
        BasePage(self.driver).assert_true(BasePage(self.driver).is_element_present(HomePage(self.driver)._shopWindow))


if __name__ == '__main__':
    unittest.main()

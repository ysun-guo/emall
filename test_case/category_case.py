# coding=utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from pages.category_page import CategoryPage
import logging
import os
from public.readConf import ReadConf
from selenium.webdriver.support import expected_conditions as ec
from pages.search_page import SearchPage
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
        BasePage(cls.driver).login_by_js(False)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url(ReadConf().readconf("URL", "categoryURL"))

    def test_page_show_check(self):
        '''
        商品分类页面元素展示
        '''
        logging.info('**验证分类页面的元素是否已经展示**')
        res = BasePage(self.driver).is_element_present(CategoryPage(self.driver)._search_box)
        if res is True:
            logging.info('搜索框展示在页面上')
        else:
            logging.warning('搜索框未出现在页面上')
        res = BasePage(self.driver).is_element_present(CategoryPage(self.driver)._cate)
        if res is True:
            logging.info('左侧前端分类展示在页面上')
        else:
            TestCase().fail('左侧前端分类未出现在页面上')
        res = BasePage(self.driver).is_element_present(CategoryPage(self.driver)._child_cate_region)
        if res is True:
            logging.info('右侧商品分类展示在页面上')
        else:
            TestCase().fail('右侧商品分类未出现在页面上')
        print(self.driver.title)
        BasePage(self.driver).check_exist_in_string('分类', self.driver.title)

    def test_click_cate(self):
        '''
        分类点击，切换选中
        '''
        logging.info('**分类是否可点击**')
        CategoryPage(self.driver).click_cate()
        res = BasePage(self.driver).is_element_present(CategoryPage(self.driver)._child_cate_region)
        if res is True:
            logging.info('右侧商品分类展示在页面上')
        else:
            TestCase().fail('右侧商品分类未出现在页面上')

    @data("优惠金额验证3")
    def test_click_search_box(self, value):
        '''
        商品分类页面搜索框
        '''
        logging.info('**搜索框是否可用**')
        CategoryPage(self.driver).click_search_box()
        res = BasePage(self.driver).is_element_present(SearchPage(self.driver)._cancel_button)
        if res is True:
            logging.info('搜索取消按钮展示在页面上')
        else:
            logging.warning('搜索取消按钮未出现在页面上')
        res = BasePage(self.driver).is_element_present(SearchPage(self.driver)._search_box)
        if res is True:
            logging.info('搜索输入框展示在页面上')
        else:
            TestCase().fail('搜索输入框未出现在页面上')
        SearchPage(self.driver).send_key_search_box(value)


if __name__ == '__main__':
    unittest.main()

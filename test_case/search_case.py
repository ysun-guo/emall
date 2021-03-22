# coding=utf-8
import unittest
from ddt import *
from public.BasePage import BasePage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from time import sleep
import logging
import os


@ddt
class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver_path = os.getcwd() + '/chromedriver'
        # driver_path = 'chromedriver'
        options = BasePage(cls).device_dev_set()
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
        BasePage(cls.driver).visit_url()
        BasePage(cls.driver).login_by_js(False)
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url()

    @data("优惠金额验证3")
    def test_search(self, value):
        '''
        输入商品名称进行搜索
        '''
        logging.info('**输入商品名称搜索，验证是否有搜索到相关商品**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box(value)
        sleep(2)
        for productName in SearchPage(self.driver).get_product_names():
            name = SearchPage(self.driver).get_element_value(productName)
            logging.info("商品名称:" + name)
            BasePage(self.driver).check_exist_in_string(value, name)

    def test_search_cancel(self):
        '''
        在搜索页，点击取消按钮，返回到上一页
        '''
        logging.info('**在搜索页面点击取消，验证是否会返回到首页**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).click_cancel_button()
        sleep(2)
        BasePage(self.driver).assert_true(BasePage(self.driver).is_element_present(HomePage(self.driver)._shopWindow))


if __name__ == '__main__':
    unittest.main()

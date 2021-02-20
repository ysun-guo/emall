# coding=utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from pages.home_page import HomePage
from public.public import get_screen_in_case_end_or_error
import logging
import os


class HomeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver_path = os.getcwd() + '/chromedriver'
        options = BasePage(cls).device_dev_set()
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
        cls.driver.implicitly_wait(5)
        BasePage(cls.driver).visit_url()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url()

    @get_screen_in_case_end_or_error
    def test_home_check(self):
        logging.info('**验证首页的橱窗、广告模板等是否已经展示**')
        HomePage(self.driver).check_shop_window_show()
        HomePage(self.driver).check_advert_show()
        HomePage(self.driver).check_product_show()
        HomePage(self.driver).check_banner_show()
        HomePage(self.driver).check_search_box_show()


if __name__ == '__main__':
    unittest.main()

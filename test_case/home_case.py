# coding=utf-8
from selenium import webdriver
import unittest
from ddt import *
from public.BasePage import BasePage
from pages.home_page import HomePage
from public.public import get_screen_in_case_end_or_error


@ddt
class HomeTest(unittest.TestCase):
    # 搜索测试
    @classmethod
    def setUpClass(cls):
        options = BasePage().device_dev_set()
        cls.driver = webdriver.Chrome(chrome_options=options)
        cls.driver.implicitly_wait(5)
        BasePage(cls.driver).visit_url()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url()

    @get_screen_in_case_end_or_error
    def test_home_check(self):
        HomePage(self.driver).check_shopwindow_show()
        HomePage(self.driver).check_advert_show()
        HomePage(self.driver).check_product_show()
        HomePage(self.driver).check_banner_show()
        HomePage(self.driver).check_search_box_show()


if __name__ == '__main__':
    unittest.main()

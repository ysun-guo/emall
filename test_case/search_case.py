# coding=utf-8
import unittest
from ddt import *
from public.BasePage import BasePage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from public.public import get_screen_in_case_end_or_error
from selenium import webdriver


@ddt
class SearchTest(unittest.TestCase):
    # '''搜索测试'''
    @classmethod
    def setUpClass(cls):
        options = BasePage(cls).device_dev_set()
        cls.driver = webdriver.Chrome(chrome_options=options)
        BasePage(cls.driver).visit_url()
        BasePage(cls.driver).login_by_js(False, '13175115726')
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url()

    # @data(("12456", "12356"), ("user02", '123456'))
    @data("限购测试")
    # @unpack
    @get_screen_in_case_end_or_error
    def test_search(self, value):
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).check_search_have_product(value)

    def test_search_cancel(self):
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).cancel_search()


if __name__ == '__main__':
    unittest.main()

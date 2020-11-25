# coding=utf-8
import unittest
from ddt import *
from public.BasePage import BasePage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from public.public import get_screen_in_case_end_or_error
from selenium import webdriver
import public.my_var
@ddt
class SearchTest(unittest.TestCase):
    '''搜索测试'''

    def setUp(self):
        global token
        options=public.my_var.return_driver_option()
        self.driver=webdriver.Chrome(chrome_options=options)
        BasePage(self.driver).visit_url()
        token=BasePage(self.driver).login_by_js(False)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

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

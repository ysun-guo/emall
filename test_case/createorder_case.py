# coding=utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from pages.createorder_page import CheckCreatOrder,CreateOrderPage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from public.public import get_screen_in_case_end_or_error
from ddt import data,ddt

@ddt
class CreateOrderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = BasePage(cls).device_dev_set()
        cls.driver = webdriver.Chrome(chrome_options=options)
        cls.driver.implicitly_wait(5)
        BasePage(cls.driver).visit_url()
        BasePage(cls.driver).login_by_js(True)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url()

    # 提交订单页的页面元素检查
    # @data("限购测试")
    # @get_screen_in_case_end_or_error
    # def test_create_order_info_check(self,value):
    #     HomePage(self.driver).click_search_box()
    #     SearchPage(self.driver).send_key_search_box()
    #     SearchPage(self.driver).click_search_product_01()
    #     ProductPage(self.driver).product_buy(value)
    #     CheckCreatOrder(self.driver).check_page_is_show()

    # 点击提交订单按钮，检查
    @data("限购测试")
    @get_screen_in_case_end_or_error
    def test_create_order_check(self,value):
        expected = None
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).product_buy(value)
        CreateOrderPage(self.driver).click_creat_order_btn()
        CheckCreatOrder(self.driver).check_create_order(expected)

if __name__ == '__main__':
    unittest.main()

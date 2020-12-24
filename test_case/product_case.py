# coding=utf-8
from selenium import webdriver
import unittest
from ddt import *
from public.BasePage import BasePage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from public.public import get_screen_in_case_end_or_error


class ProductTest(unittest.TestCase):

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

    @get_screen_in_case_end_or_error
    def test_product_add_to_car(self, value=2):
        # 商铺详情页点击加入购物车'''
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        before = ProductPage(self.driver).get_car_num_value()
        ProductPage(self.driver).product_add_to_car(value)
        after = ProductPage(self.driver).get_car_num_value()
        ProductPage(self.driver).check_add_to_car(
            before=before,
            value=value,
            after=after
        )

    @get_screen_in_case_end_or_error
    def test_sku_add_to_car(self, value=2):
        # 打开规格详情加入购物车'''
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        before = ProductPage(self.driver).get_car_num_value()
        ProductPage(self.driver).product_sku_add_to_car(value)
        after = ProductPage(self.driver).get_car_num_value()
        ProductPage(self.driver).check_add_to_car(
            before=before,
            value=value,
            after=after)

    @get_screen_in_case_end_or_error
    def test_product_buy(self, value=2):
        # '''商品详情点击立即购买'''
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).product_buy(value)
        ProductPage(self.driver).check_buy()

    @get_screen_in_case_end_or_error
    def test_sku_buy(self, value=2):
        # '''打开规格详情立即购买'''
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).product_sku_buy(value)
        ProductPage(self.driver).check_buy()

    @get_screen_in_case_end_or_error
    def test_return_home(self):
        # '''首页按钮返回'''
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).click_home_button()
        ProductPage(self.driver).check_return_home()


    @get_screen_in_case_end_or_error
    def test_go_to_cart(self):
        # '''购物车按钮跳转'''
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).click_cart_button()
        ProductPage(self.driver).check_go_to_cart()


if __name__ == '__main__':
    unittest.main()

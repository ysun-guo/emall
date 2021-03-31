# coding=utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from pages.createorder_page import CreateOrderPage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from ddt import data, ddt, unpack
from selenium.webdriver.support import expected_conditions as ec

from time import sleep
import os
from unittest import TestCase
from selenium.common import exceptions


@ddt
class CreateOrderTest(unittest.TestCase):

    product_name = '优惠金额验证'

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

    @data([product_name, 1])
    @unpack
    def test_create_order_check(self, product_name, num):
        '''
        在支付页面元素校验
        '''
        print('**在商品详情页，点击提交订单，验证是否跳转到提交订单页面**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box(product_name)
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).product_buy(num)
        CreateOrderPage(self.driver).click_creat_order_btn()
        sleep(2)
        BasePage(self.driver).assert_true(ec.url_contains('pages/pay/pay?orderId'))
        BasePage(self.driver).assert_true(ec.title_is('订单支付'))
        BasePage(self.driver).assert_true(BasePage(self.driver).is_element_present(CreateOrderPage(self.driver)._pay_btn))
        print("提交订单按钮已展示")
        BasePage(self.driver).assert_true(BasePage(self.driver).is_element_present(CreateOrderPage(self.driver)._pay_fee_form))
        print("价格区域已展示")
        # 点击立即支付按钮
        CreateOrderPage(self.driver).click_pay_btn()
        # 断言有没有报错
        try:
            toast_txt = BasePage(self.driver).get_toast_text()
            TestCase().fail("支付报错：" + toast_txt)
        except exceptions.TimeoutException:
            BasePage(self.driver).assert_true(ec.url_contains('prepay_id=wx'))

    @data([product_name, 1])
    @unpack
    def test_create_order_info_check(self, product_name, num):
        '''
        提交订单页面元素检查
        '''
        print('**从商品详情页，点击立即购买，验证是否跳转到提交订单页**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box(product_name)
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).product_buy(num)
        sleep(2)
        BasePage(self.driver).assert_true(BasePage(self.driver).is_element_present(CreateOrderPage(self.driver)._addr_form))
        print("收货人地址栏已展示")
        BasePage(self.driver).assert_true(BasePage(self.driver).is_element_present(CreateOrderPage(self.driver)._product_list_form))
        print("商品列表已展示")
        BasePage(self.driver).assert_true(BasePage(self.driver).is_element_present(CreateOrderPage(self.driver)._order_fee_form))
        print("金额计算区域已展示")
        BasePage(self.driver).assert_true(BasePage(self.driver).is_element_present(CreateOrderPage(self.driver)._create_order_btn_form))
        print("提交订单按钮栏已展示")


if __name__ == '__main__':
    unittest.main()

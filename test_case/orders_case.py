# coding:utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from pages.order_page import OrderPage
from pages.home_page import HomePage
from public.readConf import ReadConf

from unittest import TestCase


class OrdersTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        return_list = BasePage(cls).class_setup_set(True)
        cls.driver = return_list[0]
        cls.token = return_list[1]

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url(ReadConf().readconf("URL", "ordersURL"))

    def test_orders_info_check(self):
        '''
        检查订单列表的商品信息是否展示
        '''
        res = BasePage(self.driver).is_element_present(OrderPage(self.driver)._order_code)
        if res is True:
            print('订单编号模块已展示')
        else:
            TestCase().fail("订单编号模块未展示")
        res = BasePage(self.driver).is_element_present(OrderPage(self.driver)._order_product_spec)
        if res is True:
            print('订单商品规格模块已展示')
        else:
            TestCase().fail("订单商品规格模块未展示")
        BasePage(self.driver).is_element_present(OrderPage(self.driver)._order_product_name)
        if res is True:
            print('订单商品名称模块已展示')
        else:
            TestCase().fail("订单商品名称模块未展示")
        BasePage(self.driver).is_element_present(OrderPage(self.driver)._order_product_price)
        if res is True:
            print('订单商品价格模块已展示')
        else:
            TestCase().fail("订单商品价格模块未展示")
        BasePage(self.driver).is_element_present(OrderPage(self.driver)._order_product_num)
        if res is True:
            print('订单商品数量模块已展示')
        else:
            TestCase().fail("订单商品数量模块未展示")


if __name__ == '__main__':
    unittest.main()

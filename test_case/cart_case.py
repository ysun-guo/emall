# coding=utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from pages.cart_page import CartPage
from pages.cart_page import CartApi
from pages.product_page import ProductPage
from pages.createorder_page import CreateOrderPage
from public.readConf import ReadConf
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

from unittest import TestCase
import os


class CartTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        return_list = BasePage(cls).class_setup_set(True)
        cls.driver = return_list[0]
        cls.token = return_list[1]

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url(ReadConf().readconf("URL", "cartURL"))

    def test_page_show(self):
        '''
        购物车展示元素校验
        '''
        print('**购物车页面元素校验**')
        print('**左上角的商品总数与接口进行比对**')
        page_total_num = CartPage(self.driver).get_cart_total_num()
        api_total_num = CartApi.get_cart_total_num_api(self.token)
        BasePage(self.driver).assert_equal(int(page_total_num), api_total_num)
        print('**购物车列表的商品名称和商品数量与接口进行比对**')
        page_product_name_list = CartPage(self.driver).get_product_name_list()
        page_product_num_list = CartPage(self.driver).get_product_num_text()
        page_product_num_list = [int(i) for i in page_product_num_list]  # 全部转成int类型
        page_product_info = [page_product_name_list, page_product_num_list]
        api_product_info_list = CartApi.get_cart_list_api(self.token)
        api_product_info = []
        for api_product_infos in api_product_info_list:
            api_product_info.append(api_product_infos[1:])
        api_product_info = list(map(list, zip(*api_product_info)))  # 行列转换
        print(page_product_info)
        print(api_product_info)
        TestCase().assertListEqual(page_product_info, api_product_info)

    # def test_modify_num(self):
    #     pass
    #
    # def test_del_product(self):
    #     pass
    #
    # def test_multiple_del_product(self):
    #     pass
    #
    def test_product_detail(self):
        '''
        购物车商品，点击跳转到商品详情页
        '''
        print('**在购物车列表，点击第一个商品详情，验证是否跳转到商品详情页面**')
        product_name = CartPage(self.driver).get_product_name_list()
        CartPage(self.driver).click_product_name_01()
        sleep(2)
        product_detail_name = ProductPage(self.driver).get_product_name()
        BasePage(self.driver).assert_equal(product_name[0], product_detail_name)
        ec.url_contains("pages/product/detail?id")
        ec.title_is("商品详情")
    #
    # def test_switch_sku(self):
    #     pass

    def test_create_order(self):
        '''
        购物车商品，选中，点击结算，跳转到提交订单页
        '''
        print('**从购物车列表，点击结算，验证跳转到提交订单页**')
        # 修改商品数量

        CartPage(self.driver).input_product_num(1)
        CartPage(self.driver).click_product_select_icon()
        CartPage(self.driver).click_create_order_btn()
        sleep(3)
        ec.title_contains('提交订单')
        ec.url_contains('emall/pages/order/createOrder')
        res = BasePage(self.driver).is_element_present(CreateOrderPage(self)._product_list_form)
        if res is True:
            print('商品模块已展示')
        else:
            TestCase().fail('商品模块未展示')

    def test_create_order_no_product(self):
        '''
        购物车商品，不选择，点击结算，提示
        '''
        print('**在购物车页面，不勾选商品，直接点击结算，校验是否有预期的toast**')
        CartPage(self.driver).click_create_order_btn()
        flag = BasePage(self.driver).is_show_toast()
        BasePage(self.driver).assert_equal(flag, True)
        toast_text = BasePage(self.driver).get_toast_text()
        expected_toast_text = '请选择需要结算的商品'
        BasePage(self.driver).assert_true(toast_text in expected_toast_text)


if __name__ == "__main__":
    unittest.main()

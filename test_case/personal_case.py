# coding=utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from pages.personal_page import PersonalPage
from pages.order_page import OrderPage
import logging
import os
from public.readConf import ReadConf
from selenium.webdriver.support import expected_conditions as ec
from ddt import ddt, data
from unittest import TestCase
import time


@ddt
class PersoanlTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        return_list = BasePage(cls).class_setup_set(True)
        cls.driver = return_list[0]
        cls.token = return_list[1]

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(
            self.driver).visit_url(
            ReadConf().readconf(
                "URL",
                "personalURL"))

    def test_page_show_check(self):
        '''
        我的页面元素展示
        '''
        logging.info('**验证我的页面的元素是否已经展示**')
        res = BasePage(
            self.driver).is_element_present(
            PersonalPage(
                self.driver)._order)
        if res is True:
            logging.info('订单模块显示在页面上')
        else:
            TestCase().fail('页面中未找到订单模块')
        BasePage(
            self.driver).assert_true(
            BasePage(
                self.driver).is_element_present(
                PersonalPage(
                    self.driver)._distribution))
        BasePage(
            self.driver).assert_true(
            BasePage(
                self.driver).is_element_present(
                PersonalPage(
                    self.driver)._member_info))
        BasePage(
            self.driver).assert_true(
            BasePage(
                self.driver).is_element_present(
                PersonalPage(
                    self.driver)._other_item))
        BasePage(
            self.driver).assert_true(
            BasePage(
                self.driver).is_element_present(
                PersonalPage(
                    self.driver)._saas_link))
        BasePage(self.driver).check_exist_in_string('我的', self.driver.title)

    def test_all_order_link(self):
        '''
        点击全部订单跳转
        '''
        logging.info("**我的页面元素是否展示**")
        PersonalPage(self.driver).click_all_order_link()
        BasePage(self.driver).check_exist_in_string('我的订单', self.driver.title)
        BasePage(
            self.driver).check_exist_in_string(
            'myOrders',
            self.driver.current_url)
        delivery_method_tab_classname = BasePage(self.driver).get_element_attribute(
            OrderPage(self.driver).get_delivery_method_tab(1), 'className')
        time.sleep(5)
        delivery_method_tab_innertext = BasePage(self.driver).get_element_attribute(
            OrderPage(self.driver).get_delivery_method_tab(1), 'innerText')
        order_state_tab_classname = BasePage(
            self.driver).get_element_attribute(
            OrderPage(
                self.driver).get_order_state_tab(1),
            'className')
        order_state_tab_innertext = BasePage(
            self.driver).get_element_attribute(
            OrderPage(
                self.driver).get_order_state_tab(1),
            'innerText')
        BasePage(
            self.driver).check_exist_in_string(
            'switchLeft',
            delivery_method_tab_classname)
        BasePage(self.driver).check_exist_in_string(
            '快递配送', delivery_method_tab_innertext)
        BasePage(self.driver).check_exist_in_string(
            'seletTitle', order_state_tab_classname)
        BasePage(
            self.driver).check_exist_in_string(
            '全部', order_state_tab_innertext)

    @data(1, 2, 3, 4, 5)
    def test_state_order_link(self, n):
        '''
        点击待支付、待自提等跳转到对应的订单列表中
        '''
        logging.info("**我的订单模块点击进入不同tab页**")
        expected_deliver_class_name = 'switchLeft'
        expected_deliver_inner_text = ['快递配送', '门店自提']
        expected_order_state_class_name = 'seletTitle'
        expected_order_state_inner_text = [['全部', '全部'], ['待支付', '待支付'], ['待成团', '待成团'], ['待发货', '待自提'], ['待收货', '已完成']]
        if n == 1 or n == 2 or n == 3 or n == 4:
            m = 1
            x = n + 1
        if n == 5:
            m = 2
            x = 4
        PersonalPage(self.driver).click_state_order_link(n)
        BasePage(self.driver).check_exist_in_string('我的订单', self.driver.title)
        BasePage(
            self.driver).check_exist_in_string(
            'myOrders',
            self.driver.current_url)
        delivery_method_tab_classname = BasePage(self.driver).get_element_attribute(
            OrderPage(self.driver).get_delivery_method_tab(m), 'className')
        delivery_method_tab_innertext = BasePage(self.driver).get_element_attribute(
            OrderPage(self.driver).get_delivery_method_tab(m), 'innerText')
        order_state_tab_classname = BasePage(self.driver).get_element_attribute(
            OrderPage(self.driver).get_order_state_tab(x), 'className')
        order_state_tab_innertext = BasePage(
            self.driver).get_element_attribute(
            OrderPage(self.driver).get_order_state_tab(x), 'innerText')
        BasePage(
            self.driver).check_exist_in_string(
            expected_order_state_class_name,
            order_state_tab_classname)
        BasePage(self.driver).assert_equal(order_state_tab_innertext,
                                           expected_order_state_inner_text[x - 1][m - 1])
        if n == 1 or n == 2 or n == 3 or n == 4:
            BasePage(
                self.driver).assert_equal(
                delivery_method_tab_classname,
                expected_deliver_class_name)
            BasePage(
                self.driver).check_exist_in_string(
                expected_deliver_inner_text[0],
                delivery_method_tab_innertext)
            BasePage(self.driver).assert_equal(order_state_tab_innertext,
                                               expected_order_state_inner_text[x - 1][m - 1])
        if n == '5':
            BasePage(
                self.driver).assert_equal(
                delivery_method_tab_classname,
                expected_deliver_class_name)
            BasePage(
                self.driver).check_exist_in_string(
                expected_deliver_inner_text[1],
                delivery_method_tab_innertext)


if __name__ == '__main__':
    unittest.main()

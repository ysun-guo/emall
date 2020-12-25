# coding=utf-8

from public.BasePage import BasePage
from unittest import TestCase
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import requests
from public.readConf import ReadConf
from cart_page import CartPage
from time import sleep
from public.public import check_page


class CreateOrderPage(BasePage):

    _addr_form = (By.CLASS_NAME, 'select-address')
    _product_list_form = (By.CLASS_NAME, 'product-list')
    _order_fee_form = (By.CLASS_NAME, 'order-fee-items')
    _create_order_btn_form = (By.CLASS_NAME, 'created-order-btn')
    _create_order_btn = (By.CLASS_NAME, 'submit-order')
    _pay_btn = (By.CLASS_NAME, 'payBtn')
    _pay_fee_form = (By.CLASS_NAME, 'payConent')

    def get_addr_form(self):
        self.find_element(self._addr_form)

    def get_product_list_form(self):
        self.find_element(self._product_list_form)

    def get_order_fee_form(self):
        self.find_element(self._order_fee_form)

    def get_create_order_btn_form(self):
        self.find_element(self._create_order_btn_form)

    def click_creat_order_btn(self):
        self.click_element(self._create_order_btn)

    def get_pay_btn(self):
        self.find_element(self._pay_btn)

    def get_pay_fee_form(self):
        self.find_element(self._pay_fee_form)


class CheckCreatOrder(CreateOrderPage, BasePage):
    def check_page_is_show(self):
        self.assert_true(
            ec.visibility_of_element_located(
                self.get_addr_form()))
        logging.info("收货人地址栏已展示")
        self.assert_true(
            ec.visibility_of_element_located(
                self.get_product_list_form()))
        logging.info("商品列表已展示")
        self.assert_true(
            ec.visibility_of_element_located(
                self.get_order_fee_form()))
        logging.info("金额计算区域已展示")
        self.assert_true(
            ec.visibility_of_element_located(
                self.get_create_order_btn_form()))
        logging.info("提交订单按钮栏已展示")

    @check_page
    def check_create_order(self, expected):
        sleep(2)
        # ***********加是否成功创建订单的判断***************
        ec.url_contains('pages/pay/pay?orderId')
        ec.title_is('订单支付')
        self.assert_true(ec.visibility_of_element_located(self.get_pay_btn()))
        logging.info("提交订单按钮已展示")
        self.assert_true(ec.visibility_of_element_located(self.get_pay_fee_form()))
        logging.info("价格区域已展示")

# coding=utf-8

from public.BasePage import BasePage
from selenium.webdriver.common.by import By


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

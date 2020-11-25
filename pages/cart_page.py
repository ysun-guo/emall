# coding=utf-8

from public.BasePage import BasePage
from unittest import TestCase
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests
import public.my_var


# 继承于Basepage
class CartPage(BasePage):
    '''购物车页面数据获取'''
    # 底下导航栏的购物车按钮
    _cart_bar = (By.XPATH, '//div[@class="uni-tabbar__item"][3]')
    # 购物车共X件宝贝
    _cart_total_num = (
        By.XPATH,
        '//uni-view[@class="cart-count"]/uni-text/span')
    # 批量操作的编辑/完成按钮
    _cart_edit_btn = (By.CLASS_NAME, 'cart-edit')
    # 批量操作的删除按钮
    _cart_edit_delete_btn = (By.CLASS_NAME, 'complate-btn')
    # 数量-按钮
    _product_num_del = (By.XPATH, 'uni-view[@class="product-del"][1]')
    # 数量+按钮
    _product_num_add = (By.XPATH, 'uni-view[@class="product-add"][1]')
    # 数量输入框
    _product_num_input = (By.XPATH, 'input[@class="uni-input-input"][1]')
    # 多规格商品的规格按钮
    _product_sku_choose_btn = (
        By.XPATH,
        'uni-view[@class="product-sku-select-down flex-center overflow-ellipsis-1"][1]')
    # sku的选择弹窗
    _product_sku_choose_box = (
        By.XPATH, 'uni-view[@class="product-sku-select-inner"]')
    # 结算按钮
    _create_order_btn = (By.CLASS_NAME, 'create-order-btn')
    # 合计金额
    _count_money = (By.XPATH, '//uni-view[@class="count-money"]/uni-text/span')
    # 全选按钮
    _select_all_btn = (By.CLASS_NAME, 'select-all-btn')
    # toast提示
    _toast_text = (By.XPATH, '//*[@text="请选择需要结算的商品"]')
    # 去逛逛按钮
    _goto_anywhere_btn = (By.CLASS_NAME, 'look-otherwhere')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    '''元素定位层'''

    # 批量编辑/完成按钮
    def get_cart_edit_btn(self):
        return self.find_element(self._cart_edit_btn)

    # 批量编辑的删除按钮
    def get_cart_edit_delete_btn(self):
        return self.find_element(self._cart_edit_delete_btn)

    # 购物车共x件宝贝的text
    def get_cart_total_num_text(self):
        return self.find_element(self._cart_total_num)

    # 商品数量输入框
    def get_product_num_input_box(self):
        return self.find_element(self._product_num_input)

    def get_toast_text(self):
        return self.find_element(self._toast_text)

    '''元素操作层'''

    # 点击去逛逛
    def click_goto_anywhere_btn(self):
        self.click_element(self._goto_anywhere_btn)

    # 点击购物车导航
    def click_cart_bar(self):
        self.click_element(self._cart_bar)

    # 获取购物车商品总数
    def get_cart_total_num(self):
        return self.get_element_value(self.get_cart_total_num_text())

    # 点击编辑/完成按钮
    def click_cart_edit_btn(self):
        self.click_element(self._cart_edit_btn)

    # 点击删除按钮
    def click_cart_edit_delete_btn(self):
        self.click_element(self._cart_edit_delete_btn)

    # 点击商品数量+
    def click_product_num_add(self):
        self.click_element(self._product_num_add)

    # 点击商品数量-
    def click_product_num_del(self):
        self.click_element(self._product_num_del)

    # 输入商品数量
    def input_product_num(self, num):
        self.sendkey_element(self.get_product_num_input_box(), num)

    # 获取商品数量
    def get_product_num_text(self):
        self.get_element_value(self.get_product_num_input_box())
    # 通过api获取购物车信息：id，productname，num


class CartApi():
    '''api获取数据'''

    def get_cart_list(self, token):
        '''获取用户的购物车列表id，name，num'''
        api = '/api/v1/shopping/cart/list'
        host = public.my_var.test_host
        url = host + api
        header = {
            "token": token,
            "tenantId": "100108"
        }
        req = requests.get(url, headers=header)
        text = req.json()
        texts = text["body"]
        cart_product_info_list = []
        for text in texts:
            cart_id = text["id"]
            num = text["num"]
            product_name = text["product"]["name"]
            cart_product_info_list.append([cart_id, product_name, num])
        return cart_product_info_list

    def delete_cart(self):
        '''从购物车里删除'''
        pass


class CartCheck(BasePage):
    '''购物车逻辑断言'''

    def check_toast_text(self):
        try:
            WebDriverWait(
                self.driver, 5, 0.5).until(
                EC.presence_of_element_located(
                    CartPage.get_toast_text()))
            print("获取到toast提示")
        except BaseException:
            print("未获取到toast提示")

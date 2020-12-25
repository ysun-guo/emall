# coding=utf-8

from BasePage import BasePage
from unittest import TestCase
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from public.public import check_page
import requests
from readConf import ReadConf
from product_page import ProductPage
from time import sleep


class CartPage(BasePage):
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
    _product_num_del = (By.XPATH, '//uni-view[@class="product-del"]')
    # 数量+按钮
    _product_num_add = (By.XPATH, '//uni-view[@class="product-add"]')
    # 数量输入框
    _product_num_input = (By.XPATH, '//input[@class="uni-input-input"]')
    # 多规格商品的规格按钮
    _product_sku_choose_btn = (
        By.XPATH,
        '//uni-view[@class="product-sku-select-down flex-center overflow-ellipsis-1"]')
    # sku的选择弹窗
    _product_sku_choose_box = (
        By.XPATH, '//uni-view[@class="product-sku-select-inner"]')
    # 结算按钮
    _create_order_btn = (By.CLASS_NAME, 'create-order-btn')
    # 合计金额
    _count_money = (By.XPATH, '//uni-view[@class="count-money"]/uni-text/span')
    # 全选按钮
    _select_all_btn = (By.CLASS_NAME, 'select-all-btn')
    # 去逛逛按钮
    _goto_anywhere_btn = (By.CLASS_NAME, 'look-otherwhere')
    # 商品名称
    _product_name = (
        By.XPATH,
        '//uni-view[@class="pruduct-name overflow-ellipsis-1"]')
    # 删除弹窗的确定按钮
    _del_popup_sure_btn = (
        By.CLASS_NAME,
        'uni-modal__btn uni-modal__btn_primary')
    # 商品前的选择按钮
    _product_select_icon = (By.XPATH, '//uni-view[@class="select-icons"]')

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
        return self.find_elements(self._product_num_input)

    def get_product_names(self):
        sleep(1)
        return self.find_elements(self._product_name)

    # 获取商品名称
    def get_product_name_list(self):
        results = []
        for product_name in self.get_product_names():
            results.append(self.get_element_value(product_name))
        return results

    # 获取购物车商品总数
    def get_cart_total_num(self):
        return self.get_element_value(self.get_cart_total_num_text())

    # 获取商品数量
    def get_product_num_text(self):
        results = []
        for product_num in self.get_product_num_input_box():
            results.append(self.get_element_attribute(product_num, "value"))
        return results

    '''元素操作层'''
    # 点击第一个商品名称

    def click_product_name_01(self):
        self.click_element(self._product_name)

    # 点击去逛逛
    def click_goto_anywhere_btn(self):
        self.click_element(self._goto_anywhere_btn)

    # 点击购物车导航
    def click_cart_bar(self):
        self.click_element(self._cart_bar)

    # 点击编辑/完成按钮
    def click_cart_edit_btn(self):
        self.click_element(self._cart_edit_btn)
    # 点击全选按钮

    def click_select_all_btn(self):
        self.click_element(self._select_all_btn)

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

    def click_del_popup_sure_btn(self):
        self.click_element(self._del_popup_sure_btn)

    def click_product_select_icon(self):
        self.click_element(self._product_select_icon)
    # 点击结算按钮

    @check_page
    def click_create_order_btn(self, expected):
        self.click_element(self._create_order_btn)


class CartApi(BasePage):
    # api获取数据

    @staticmethod
    def get_cart_list_api(token):
        # 获取用户的购物车列表id，name，num
        tenant_id = ReadConf().readconf("TenantID", "tenant_id")
        host = ReadConf().readconf("HOST", "host")
        api = '/api/v1/shopping/cart/list'
        url = host + api
        header = {
            "token": token,
            "tenantId": tenant_id
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
        # 从购物车里删除
        pass

    @staticmethod
    def get_cart_total_num_api(token):
        tenant_id = ReadConf().readconf("TenantID", "tenant_id")
        host = ReadConf().readconf("HOST", "host")
        api = '/api/v1/shopping/cart/num'
        url = host + api
        header = {
            "token": token,
            "tenantId": tenant_id
        }
        logging.info(token)
        req = requests.get(url, headers=header)
        text = req.json()
        logging.info(text)
        return text["body"]


class CartCheck(CartPage, CartApi):
    # 购物车逻辑断言

    def check_cart_total_num(self, token):
        page_total_num = self.get_cart_total_num()
        api_total_num = CartApi.get_cart_total_num_api(token)
        self.assert_equal(int(page_total_num), api_total_num)

    def check_cart_product_info(self, token):
        page_product_name_list = self.get_product_name_list()
        page_product_num_list = self.get_product_num_text()
        page_product_num_list = [int(i)
                                 for i in page_product_num_list]  # 全部转成int类型
        page_product_info = [page_product_name_list, page_product_num_list]
        api_product_info_list = CartApi.get_cart_list_api(token)
        api_product_info = []
        for api_product_infos in api_product_info_list:
            api_product_info.append(api_product_infos[1:])
        api_product_info = list(map(list, zip(*api_product_info)))  # 行列转换
        logging.info(page_product_info)
        logging.info(api_product_info)
        TestCase().assertListEqual(page_product_info, api_product_info)

    def check_cart_product_del(self, token):
        self.click_cart_edit_btn()
        try:
            self.get_cart_edit_delete_btn()
        except Exception as e:
            print(type(e), e)
            logging.warning("删除按钮未出现")

        self.click_select_all_btn()
        self.click_cart_edit_delete_btn()
        self.click_del_popup_sure_btn()
        api_product_list = CartApi.get_cart_list_api(token)
        TestCase().assertIsNone(api_product_list)
        self.check_exist_in_page("去逛逛")

    def check_goto_anywhere_btn(self):
        self.click_goto_anywhere_btn()
        self.check_exist_in_page("花更少，买更好")

    def check_create_order(self):
        self.check_exist_in_page("配送方式")

    def check_product_add_num(self):
        add_before = self.get_product_num_text()
        self.click_product_num_add()
        add_after = self.get_product_num_text()
        add_after_expected = int(add_before) + 1
        self.assert_equal(add_after, add_after_expected)
        del_before = self.get_product_num_text()
        self.click_product_num_del()
        del_after = self.get_product_num_text()
        del_after_expected = int(del_before) - 1
        self.assert_equal(del_after, del_after_expected)

    def check_goto_product_detail(self):
        product_name = self.get_product_name_list()
        self.click_product_name_01()
        sleep(2)
        product_detail_name = ProductPage(self.driver).get_product_name()
        self.assert_equal(product_name[0], product_detail_name)
        ec.url_contains("pages/product/detail?id")
        ec.title_is("商品详情")

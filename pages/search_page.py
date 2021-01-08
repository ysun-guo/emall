# coding=utf-8

from public.BasePage import BasePage
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class SearchPage(BasePage):
    # 元素定位信息
    _search_box = (By.XPATH, '//input[@class="uni-input-input"]')
    _cancel_button = (By.CLASS_NAME, 'uni-searchbar__cancel')
    _search_result_name = (By.CLASS_NAME, 'itemTitle')
    _search_result_product_01 = (By.XPATH, '//uni-view[@class="itemImg"][1]')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    '''元素定位层'''

    # 获取搜索输入框
    def get_search_box(self):
        return self.find_element(self._search_box)

    # 获取退出按钮
    def get_cancel_button(self):
        return self.find_element(self._cancel_button)

    # 定位搜索商品的名称
    def get_product_names(self):
        return self.find_elements(self._search_result_name)

    def get_product_01(self):
        return self.find_element(self._search_result_product_01)

    '''元素操作层'''

    # 输入搜索关键字
    def send_key_search_box(self, value='测试'):
        self.sendkey_element(self.get_search_box(), value)
        self.sendkey_element(self.get_search_box(), Keys.RETURN)

    # 点击取消按钮
    def click_cancel_button(self):
        self.click_element(self._cancel_button)

    def click_search_product_01(self):
        sleep(2)
        self.click_element(self._search_result_product_01)

    # 获取结果的商品名称
    def get_result_name(self):
        results = []
        for product_name in self.get_product_names():
            results.append(self.get_element_value(product_name))
        return results

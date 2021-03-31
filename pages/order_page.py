# coding=utf-8

from public.BasePage import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    # 元素定位信息
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def get_order_state_tab(self, n):
        """
        1:全部
        2：待支付
        3：待成团
        4：待发货/待自提
        5：待收货/已完成
        """
        return self.find_element(
            (By.XPATH, '//uni-view[@class="orderStatus"]/uni-view[' + str(n) + ']/uni-view'))

    def get_delivery_method_tab(self, n):
        """
        1：快递配送
        2：门店自提
        """
        return self.find_element((By.XPATH, '//uni-view[@class="switch"]/uni-view[' + str(n) + ']'))
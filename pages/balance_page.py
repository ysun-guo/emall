# coding=utf-8

from public.BasePage import BasePage
from selenium.webdriver.common.by import By


class BalancePage(BasePage):
    # 元素定位信息
    _balance_remain = (By.CLASS_NAME, 'remain-num')
    _recharge_btn = (By.CLASS_NAME, 'recharge-btn')
    _recharge_record_btn = (By.CLASS_NAME, 'recharge-record-btn')
    _all_tab = (By.XPATH, '//uni-view[@class="tabs-box"]/uni-vew[1]')
    _income_tab = (By.XPATH, '//uni-view[@class="tabs-box"]/uni-vew[2]')
    _pay_tab = (By.XPATH, '//uni-view[@class="tabs-box"]/uni-vew[3]')
    _recharge_num_input = (By.CLASS_NAME, 'uni-input-input')
    _recharge_confirm_btn = (By.CLASS_NAME, 'confirm-btn-box')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def click_recharge_btn(self):
        self.click_element(self._recharge_btn)

    def click_recharge_record_btn(self):
        self.click_element(self._recharge_record_btn)

    def input_recharge_num(self, num):
        self.sendkey_element(self.find_element(self._recharge_num_input), num)

    def click_recharge_confirm_btn(self):
        self.click_element(self._recharge_confirm_btn)


# coding=utf-8

from public.BasePage import BasePage
from selenium.webdriver.common.by import By


class CouponsPage(BasePage):
    # 元素定位信息
    _tabs = (By.CLASS_NAME, 'tabs-box')
    _coupon_exchange_record = (By.CLASS_NAME, 'coupon-record')
    _coupon_list = (By.CLASS_NAME, 'coupon-list')


    def __init__(self, driver):
        BasePage.__init__(self, driver)


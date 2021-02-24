# coding=utf-8

from public.BasePage import BasePage
from selenium.webdriver.common.by import By


class PersonalPage(BasePage):
    # 元素定位信息
    _member_info = (By.CLASS_NAME, 'my-info')
    _distribution = (By.CLASS_NAME, 'my-distribution')
    _order = (By.CLASS_NAME, 'order-items')
    _saas_link = (By.CLASS_NAME, 'link-sass')
    _other_item = (By.CLASS_NAME, 'my-other-item')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    '''元素定位层'''

    '''元素操作层'''

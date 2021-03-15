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
    _my_order_link = (By.CLASS_NAME, 'all-order')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def click_all_order_link(self):
        self.click_element(self._my_order_link)

    def click_state_order_link(self,n):
        """
        n=1:待支付
        n=2:待成团
        n=3:待发货
        n=4:待收货
        n=5:待自提
        n=6:退款/售后
        """
        self.click_element((By.XPATH, '//uni-view[@class="order-item"][position()=' + str(n) +']'))


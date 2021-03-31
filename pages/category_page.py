# coding=utf-8

from public.BasePage import BasePage
from selenium.webdriver.common.by import By
import random


class CategoryPage(BasePage):
    # 元素定位信息
    _search_box = (By.XPATH, '//uni-view[@class="uni-searchbar__box"]')
    _cate = (By.CLASS_NAME, 'claItem')
    _child_cate_region = (By.CLASS_NAME, 'pRitem')
    _cart_bar = (By.XPATH, '//div[@class="uni-tabbar__item"][2]')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    '''元素定位层'''
    # 获取搜索框
    def get_search_box(self):
        return self.find_element(self._search_box)

    # 获取左侧的分类
    def get_cate(self):
        return self.find_elements(self._cate)

    # 获取右侧子分类的区域模块
    def get_child_cate_region(self):
        return self.find_element(self._child_cate_region)

    '''元素操作层'''
    # 点击搜索框，进入搜索页面
    def click_search_box(self):
        self.click_element(self._search_box)

    def click_cate(self):
        length = len(self.get_cate())
        i = random.randint(2, length)
        _cate_path = (By.XPATH, '//uni-view[@class="claItem"][position()='+str(i)+']')
        self.click_element(_cate_path)

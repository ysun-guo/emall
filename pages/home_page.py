# coding=utf-8

from public.BasePage import BasePage
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class HomePage(BasePage):
    # 元素定位信息
    _search_box = (By.XPATH, '//uni-view[@class="uni-searchbar__box"]')
    _shopWindow = (By.CLASS_NAME, 'fenlei')
    _advert = (By.CLASS_NAME, 'adver')
    _product = (By.CLASS_NAME, 'assort')
    _banner = (By.CLASS_NAME, 'uni-swiper-slides')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    '''元素定位层'''
    # 获取搜索框

    def get_search_box(self):
        return self.find_element(self._search_box)
    # 获取橱窗的位置

    def get_shop_window(self):
        return self.find_element(self._shopWindow)
    # 获取广告位的位置

    def get_advert(self):
        return self.find_element(self._advert)
    # 获取商品分类的位置

    def get_product(self):
        return self.find_element(self._product)
    # 获取banner的位置

    def get_banner(self):
        return self.find_element(self._banner)

    '''元素操作层'''
    # 点击搜索框，进入搜索页面

    def click_search_box(self):
        self.click_element(self._search_box)

    '''业务层'''
    # 验证橱窗是否展示

    def check_shopwindow_show(self):
        self.assert_True(
            ec.visibility_of_element_located(
                self.get_shop_window()))
        logging.info("橱窗已展示")

    # 验证广告位是否展示
    def check_advert_show(self):
        self.assert_True(ec.visibility_of_element_located(self.get_advert()))
        logging.info("广告位已展示")
    # 验证商品分类是否展示

    def check_product_show(self):
        self.assert_True(ec.visibility_of_element_located(self.get_product()))
        logging.info("商品分类已展示")
    # 验证banner是否展示

    def check_banner_show(self):
        self.assert_True(ec.visibility_of_element_located(self.get_banner()))
        logging.info("banner已展示")
    # 验证搜索框是否展示

    def check_search_box_show(self):
        self.assert_True(
            ec.visibility_of_element_located(
                self.get_search_box()))
        logging.info("搜索框已展示")

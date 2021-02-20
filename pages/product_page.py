# coding=utf-8

from public.BasePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep
import logging
import random
from public.readConf import ReadConf
import requests
import re


class ProductPage(BasePage):

    _product_title = (By.CLASS_NAME, 'product-title')
    _add_to_car_button = (By.CLASS_NAME, 'add-car-btn')
    _buy_button = (By.CLASS_NAME, 'buy-btn')
    _product_detail = (By.CLASS_NAME, 'product-desc-detail')
    _product_item_value = (By.CLASS_NAME, 'detail-item-value')
    _product_car_num = (By.CLASS_NAME, 'cart-btn')
    _home_button = (By.CLASS_NAME, 'home-btn')
    _cart_button = (By.CLASS_NAME, 'cart-btn')
    # 点击规格信息，打开规格弹窗的信息
    _product_sku_add_to_car_button = (By.CLASS_NAME, 'sku-add-cart')
    _product_sku_buy_button = (By.CLASS_NAME, 'sku-right-now')
    _product_sku_input_box = (By.CLASS_NAME, 'uni-input-input')
    # 点击立即购买，加入购物车，打开的规格弹窗信息
    _product_confirm_button = (By.CLASS_NAME, 'product-confirm-btn')
    # 多规格商品，展示规格的区域
    _product_sku_area = (By.CLASS_NAME, 'product-skus')

    # 参加特价活动商品，在商品详情页上展示的原价、活动价、还剩x件、活动标签
    _special_product_origin_price = (By.XPATH, '//uni-text[@class="vip-price "]/span')
    _special_product_promotion_price = (By.XPATH, '//uni-view[@class="promotion-product-info"]/uni-view[1]/uni-text[1<position()][position()<3]')
    _special_product_promotion_stock = (By.XPATH, '//uni-text[@class="stock-state"]/span/uni-text/span')
    _special_tag = (By.XPATH, '//uni-text[@class="promotion-tag"]/span')
    # 规格弹窗上的原价（带￥）、活动价
    _special_product_sku_origin_price = (By.XPATH, '//uni-text[@class="sku-origin-price"]/span')
    _special_product_sku_promotion_price = (By.XPATH, '//uni-text[@class="sku-price"]/span')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    '''元素定位层'''

    # 商品详情页的按钮
    def find_product_title(self):
        return self.find_element(self._product_title)

    def is_multiple_sku(self):
        return self.is_element_present(self._product_sku_area)

    def get_product_name(self):
        return self.get_element_value(self.find_product_title())

    def get_product_detail(self):
        return self.find_element(self._product_detail)

    def get_product_item_value(self):
        return self.find_element(self._product_item_value)

    def get_add_to_car_button(self):
        return self.find_element(self._add_to_car_button)

    def get_buy_button(self):
        return self.find_element(self._buy_button)

    # 点击规格信息，打开规格弹窗的信息
    def get_product_sku_add_to_car_button(self):
        return self.find_element(self._product_sku_add_to_car_button)

    def get_product_sku_buy_button(self):
        return self.find_element(self._product_sku_buy_button)

    def get_product_sku_input_box(self):
        return self.find_element(self._product_sku_input_box)

    # 点击立即购买，加入购物车，打开的规格弹窗信息
    def get_product_confirm_button(self):
        return self.find_element(self._product_confirm_button)

    def get_product_car_num(self):
        return self.find_element(self._product_car_num)

    def get_home_button(self):
        return self.find_element(self._home_button)

    def get_cart_button(self):
        return self.find_element(self._cart_button)

    def find_special_product_origin_price(self):
        return self.find_element(self._special_product_origin_price)

    def find_special_product_promotion_price(self):
        return self.find_elements(self._special_product_promotion_price)

    def find_special_product_promotion_stock(self):
        return self.find_element(self._special_product_promotion_stock)

    def find_special_tag(self):
        return self.find_element(self._special_tag)

    def find_special_product_sku_origin_price(self):
        return self.find_element(self._special_product_sku_origin_price)

    def find_special_product_sku_promotion_price(self):
        return self.find_element(self._special_product_sku_promotion_price)

    def get_product_id_from_url(self):
        url = self.get_url()
        print(url)
        pattern = r'.*?id=([0-9]*)&.*'
        obj = re.match(pattern, url)
        product_id = obj.group(1)
        return product_id
    '''元素操作层'''

    def select_sku(self):
        logging.info("返回一个list，len(list)代表有几个规格类型，list[n]的值代表第n个规格类型有几个规格值")
        _sku = (By.XPATH, '//uni-view[@class="product-skus"]/uni-view')
        count = len(self.find_elements(_sku))
        for j in range(1, count+1):
            _sku_value = (By.XPATH, "//uni-view[@class='product-skus']/uni-view[" + str(j) + "]/uni-view[2]/uni-button")
            n = len(self.find_elements(_sku_value))
            x = random.randint(1, n)
            _sku_ = (By.XPATH, "//uni-view[@class='product-skus']/uni-view[" + str(j) + "]/uni-view[2]/uni-button[" + str(x) + "]")
            print(_sku_)
            self.click_element(_sku_)

    # 点击打开规格弹窗
    def click_product_item_value(self):
        self.driver.execute_script("window.scrollBy(0,500)")
        print("已滑动")
        self.click_element(self._product_item_value)

    # 点击加购物车按钮
    def click_add_to_car_button(self):
        self.driver.execute_script("window.scrollBy(0,500)")
        self.click_element(self._add_to_car_button)

    # 点击立即购买按钮
    def click_buy_button(self):
        self.click_element(self._buy_button)

    # 点击规格弹窗的加入购物车按钮
    def click_product_sku_add_to_car_button(self):
        self.click_element(self._product_sku_add_to_car_button)

    def click_product_sku_buy_button(self):
        self.click_element(self._product_sku_buy_button)

    def click_product_confirm_button(self):
        self.click_element(self._product_confirm_button)

    def get_car_num_value(self):
        sleep(10)
        str1 = self.get_element_value(self.get_product_car_num())
        car_num = 0
        print("完整的数据：" + str1)
        car_num_str = str1[:-3]
        if len(car_num_str) > 0:
            car_num = int(car_num_str)
        return car_num

    def input_product_num_box(self, num):
        self.clear_element(self.get_product_sku_input_box())
        self.sendkey_element(self.get_product_sku_input_box(), num)

    def click_home_button(self):
        self.click_element(self._home_button)

    def click_cart_button(self):
        self.click_element(self._cart_button)
        sleep(2)

    def get_page_special_price_info(self):
        logging.info('返回一个list：活动tag、原价、活动价、活动库存')
        product_origin_price = self.get_element_value(self.find_special_product_origin_price())
        product_promotion_price = ''
        for ele in self.find_special_product_promotion_price():
            part_price = self.get_element_value(ele)
            product_promotion_price = product_promotion_price + str(part_price)

        product_promotion_stock = self.get_element_value(self.find_special_product_promotion_stock())  # 还剩x件
        product_promotion_stock = product_promotion_stock[2:-1]
        product_promotion_tag = self.get_element_value(self.find_special_tag())
        # 打开规格弹窗
        self.click_product_item_value()
        sku_origin_price = self.get_element_value(self.find_special_product_sku_origin_price())
        sku_origin_price = sku_origin_price[1:]
        sku_promotion_price = self.get_element_value(self.find_special_product_sku_promotion_price())
        self.assert_equal(product_origin_price, sku_origin_price)
        self.assert_equal(product_promotion_price, sku_promotion_price)
        page_special_info_list = [product_promotion_tag, product_origin_price, product_promotion_price, product_promotion_stock]
        return page_special_info_list

    @staticmethod
    def get_api_special_price_info(product_id, token):
        host = ReadConf().readconf("HOST", "host")
        api = '/api/v1/product/emall/'+product_id+'/detail'
        tenant_id = ReadConf().readconf("Tenant", "tenant_id")
        url = host + api
        header = {
            "token": token,
            "tenantId": tenant_id
        }
        text = requests.get(url, headers=header)
        x = text.json()["body"]
        print(x)
        api_promotion_tag = x["tagList"][0]
        api_origin_price = x["originPrice"]
        api_promotion_price = x["promotionPrice"]
        api_promotion_stock = x["promotionInfo"]["leftProductNum"]
        api_origin_price = '{:g}'.format(api_origin_price)
        api_promotion_price = '{:g}'.format(api_promotion_price)
        api_promotion_stock = str(api_promotion_stock)
        api_special_info_list = [api_promotion_tag, api_origin_price, api_promotion_price, api_promotion_stock]
        return api_special_info_list

    '''业务层'''

    def product_add_to_car(self, value):
        self.click_add_to_car_button()
        if self.is_multiple_sku():
            self.select_sku()
        self.input_product_num_box(value)
        self.click_product_confirm_button()

    def product_buy(self, num):
        self.click_buy_button()
        if self.is_multiple_sku():
            self.select_sku()
        self.input_product_num_box(num)
        self.click_product_confirm_button()

    def product_sku_add_to_car(self, value):
        self.click_product_item_value()
        if self.is_multiple_sku():
            self.select_sku()
        self.input_product_num_box(value)
        self.click_product_sku_add_to_car_button()

    def product_sku_buy(self, value):
        self.click_product_item_value()
        if self.is_multiple_sku():
            self.select_sku()
        self.input_product_num_box(value)
        self.click_product_sku_buy_button()

# coding=utf-8

from BasePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class ProductPage(BasePage):

    _product_title = (By.CLASS_NAME, 'product-title')
    _product_price = (By.CLASS_NAME, 'price-header-common commonly-used')
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

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    '''元素定位层'''

    # 商品详情页的按钮
    def find_product_title(self):
        return self.find_element(self._product_title)

    def get_product_name(self):
        return self.get_element_value(self.find_product_title())

    def get_product_price(self):
        return self.find_element(self._product_price)

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

    '''元素操作层'''

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

    def input_product_num_box(self, value):
        self.clear_element(self.get_product_sku_input_box())
        self.sendkey_element(self.get_product_sku_input_box(), value)

    def click_home_button(self):
        self.click_element(self._home_button)

    def click_cart_button(self):
        self.click_element(self._cart_button)
        sleep(2)

    '''业务层'''

    def product_add_to_car(self, value):
        self.click_add_to_car_button()
        self.input_product_num_box(value)
        self.click_product_confirm_button()

    def product_buy(self, value):
        self.click_buy_button()
        self.input_product_num_box(value)
        self.click_product_confirm_button()

    def product_sku_add_to_car(self, value):
        self.click_product_item_value()
        self.input_product_num_box(value)
        self.click_product_sku_add_to_car_button()

    def product_sku_buy(self, value):
        self.click_product_item_value()
        self.input_product_num_box(value)
        self.click_product_sku_buy_button()

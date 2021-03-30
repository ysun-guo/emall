# coding=utf-8
from selenium import webdriver
import unittest
import logging
from public.BasePage import BasePage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from ddt import data, unpack, ddt
import os


@ddt
class ProductTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        return_list = BasePage(cls).class_setup_set(True)
        cls.driver = return_list[0]
        cls.token = return_list[1]

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url()

    def test_sku_add_to_car(self, value=2):
        '''
        从商品详情的规格弹窗，加入购物车
        '''
        logging.info('**在商品详情页，打开规格弹窗，点击加入购物车，验证购物车商品数量是否增加**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        before = ProductPage(self.driver).get_car_num_value()
        ProductPage(self.driver).product_sku_add_to_car(value)
        after = ProductPage(self.driver).get_car_num_value()
        after_expected = int(before) + int(value)
        BasePage(self.driver).assert_equal(int(after), after_expected)

    def test_product_buy(self, value=2):
        '''
        在商品详情页，点击立即购买
        '''
        logging.info('**在商品详情页，点击立即购买，验证是否跳转到提交订单页**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).product_buy(value)
        BasePage(self.driver).assert_true(ec.title_contains('提交订单'))
        BasePage(self.driver).assert_true(ec.url_contains('/pages/order/createOrder'))

    def test_sku_buy(self, value=1):
        '''
        从商品详情页的规格弹窗，点击立即购买
        '''
        logging.info('**在商品详情页，打开规格弹窗，点击立即购买，验证是否跳转到提交订单页**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        sleep(2)
        ProductPage(self.driver).product_sku_buy(value)
        BasePage(self.driver).assert_true(ec.title_contains('提交订单'))
        BasePage(self.driver).assert_true(ec.url_contains('/pages/order/createOrder'))

    def test_return_home(self):
        '''
        商品详情页的返回主页按钮
        '''
        logging.info('**在商品详情页，点击左下角的首页按钮，验证是否跳转到首页**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).click_home_button()
        BasePage(self.driver).assert_true(BasePage(self.driver).is_element_present(HomePage(self.driver)._product))

    def test_go_to_cart(self):
        '''
        商品详情页的跳转到购物车
        '''
        logging.info('**在商品详情页，点击左下角的购物车按钮，验证是否跳转到购物车页面**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).click_cart_button()
        BasePage(self.driver).assert_true(ec.title_contains('购物车'))
        BasePage(self.driver).assert_true(ec.url_contains('emall/pages/myCart/myCart'))
        
    @data("蓝月亮茶清天然绿茶洗洁精500g")
    def test_special_product_info_check(self, value):
        '''
        秒杀活动的商品详情元素校验
        '''
        logging.info('**在商品详情页，与接口返回进行对比，验证特价活动的商品价格是否展示正确**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box(value)
        SearchPage(self.driver).click_search_product_01()
        product_id = ProductPage(self.driver).get_product_id_from_url()
        page_special_info_list = ProductPage(self.driver).get_page_special_price_info()
        logging.info(page_special_info_list)
        api_special_info_list = ProductPage(self.driver).get_api_special_price_info(product_id=product_id, token=self.token)
        logging.info(api_special_info_list)
        self.assertListEqual(page_special_info_list, api_special_info_list)

    @data(["优惠金额验证3", 1])
    @unpack
    def test_product_add_to_car(self, value, num):
        '''
        商品详情页，点击加入购物车
        '''
        logging.info('**在商品详情页，点击加入购物车，验证购物车的商品数量是否对应增加**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box(value)
        SearchPage(self.driver).click_search_product_01()
        before = ProductPage(self.driver).get_car_num_value()
        ProductPage(self.driver).product_add_to_car(num)
        after = ProductPage(self.driver).get_car_num_value()
        after_expected = int(before) + int(num)
        BasePage(self.driver).assert_equal(int(after), after_expected)


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(ProductTest('test_special_product_info_check'))
    # unittest.TextTestRunner(verbosity=2).run(suite)

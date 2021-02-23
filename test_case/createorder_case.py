# coding=utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from pages.createorder_page import CreateOrderPage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from public.public import get_screen_in_case_end_or_error
from ddt import data, ddt, unpack
from selenium.webdriver.support import expected_conditions as ec
import logging
from time import sleep
import os


@ddt
class CreateOrderTest(unittest.TestCase):

    product_name = '优惠金额验证3'

    @classmethod
    def setUpClass(cls):
        driver_path = os.getcwd() + '/chromedriver'
        # driver_path = 'chromedriver'
        options = BasePage(cls).device_dev_set()
        cls.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
        cls.driver.implicitly_wait(5)
        BasePage(cls.driver).visit_url()
        BasePage(cls.driver).login_by_js(True)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url()

    @data([product_name, 1])
    @unpack
    @get_screen_in_case_end_or_error
    def test_create_order_check(self, product_name, num):
        logging.info('**在提交订单页，点击提交订单，验证是否跳转到支付页面**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box(product_name)
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).product_buy(num)
        CreateOrderPage(self.driver).click_creat_order_btn()
        sleep(2)
        BasePage(self.driver).assert_true(ec.url_contains('pages/pay/pay?orderId'))
        BasePage(self.driver).assert_true(ec.title_is('订单支付'))
        BasePage(self.driver).assert_true(ec.visibility_of_element_located(CreateOrderPage(self.driver).get_pay_btn()))
        logging.info("提交订单按钮已展示")
        BasePage(self.driver).assert_true(ec.visibility_of_element_located(CreateOrderPage(self.driver).get_pay_fee_form()))
        logging.info("价格区域已展示")

    @data([product_name, 1])
    @unpack
    @get_screen_in_case_end_or_error
    def test_create_order_info_check(self, product_name, num):
        logging.info('**从商品详情页，点击立即购买，验证是否跳转到提交订单页**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box(product_name)
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).product_buy(num)
        sleep(2)
        BasePage(self.driver).assert_true(ec.visibility_of_element_located(CreateOrderPage(self.driver).get_addr_form()))
        logging.info("收货人地址栏已展示")
        BasePage(self.driver).assert_true(ec.visibility_of_element_located(CreateOrderPage(self.driver).get_product_list_form()))
        logging.info("商品列表已展示")
        BasePage(self.driver).assert_true(ec.visibility_of_element_located(CreateOrderPage(self.driver).get_order_fee_form()))
        logging.info("金额计算区域已展示")
        BasePage(self.driver).assert_true(ec.visibility_of_element_located(CreateOrderPage(self.driver).get_create_order_btn_form()))
        logging.info("提交订单按钮栏已展示")


if __name__ == '__main__':
    unittest.main()

# coding=utf-8
from selenium import webdriver
import unittest
import logging
from public.BasePage import BasePage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from public.public import get_screen_in_case_end_or_error
from time import sleep
from selenium.webdriver.support import expected_conditions as ec

class ProductTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        options = BasePage(cls).device_dev_set()
        cls.driver = webdriver.Chrome(chrome_options=options)
        cls.driver.implicitly_wait(5)
        BasePage(cls.driver).visit_url()
        BasePage(cls.driver).login_by_js(True)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url()

    @get_screen_in_case_end_or_error
    def test_product_add_to_car(self, value=2):
        # 商铺详情页点击加入购物车'''
        logging.info('**在商品详情页，点击加入购物车，验证购物车的商品数量是否对应增加**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        before = ProductPage(self.driver).get_car_num_value()
        ProductPage(self.driver).product_add_to_car(value)
        after = ProductPage(self.driver).get_car_num_value()
        after_expected = int(before) + int(value)
        BasePage(self.driver).assert_equal(int(after), after_expected)

    @get_screen_in_case_end_or_error
    def test_sku_add_to_car(self, value=2):
        logging.info('**在商品详情页，打开规格弹窗，点击加入购物车，验证购物车商品数量是否增加**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        before = ProductPage(self.driver).get_car_num_value()
        ProductPage(self.driver).product_sku_add_to_car(value)
        after = ProductPage(self.driver).get_car_num_value()
        after_expected = int(before) + int(value)
        BasePage(self.driver).assert_equal(int(after), after_expected)

    @get_screen_in_case_end_or_error
    def test_product_buy(self, value=2):
        logging.info('**在商品详情页，点击立即购买，验证是否跳转到提交订单页**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).product_buy(value)
        BasePage(self.driver).assert_true(ec.title_contains('提交订单'))
        BasePage(self.driver).assert_true(ec.url_contains('/pages/order/createOrder'))


    @get_screen_in_case_end_or_error
    def test_sku_buy(self, value=2):
        logging.info('**在商品详情页，打开规格弹窗，点击立即购买，验证是否跳转到提交订单页**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        sleep(2)
        ProductPage(self.driver).product_sku_buy(value)
        BasePage(self.driver).assert_true(ec.title_contains('提交订单'))
        BasePage(self.driver).assert_true(ec.url_contains('/pages/order/createOrder'))

    @get_screen_in_case_end_or_error
    def test_return_home(self):
        logging.info('**在商品详情页，点击左下角的首页按钮，验证是否跳转到首页**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).click_home_button()
        HomePage(self.driver).check_product_show()


    @get_screen_in_case_end_or_error
    def test_go_to_cart(self):
        logging.info('**在商品详情页，点击左下角的购物车按钮，验证是否跳转到购物车页面**')
        HomePage(self.driver).click_search_box()
        SearchPage(self.driver).send_key_search_box()
        SearchPage(self.driver).click_search_product_01()
        ProductPage(self.driver).click_cart_button()
        BasePage(self.driver).assert_true(ec.title_contains('购物车'))
        BasePage(self.driver).assert_true(ec.url_contains('emall/pages/myCart/myCart'))



if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(ProductTest('test_sku_buy'))
    unittest.TextTestRunner(verbosity=2).run(suite)

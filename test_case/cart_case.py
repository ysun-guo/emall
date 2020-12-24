# coding=utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from cart_page import CartCheck
from cart_page import CartPage
from public.readConf import ReadConf
from public.public import get_screen_in_case_end_or_error
from time import sleep


class CartTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = BasePage(cls).device_dev_set()
        cls.driver = webdriver.Chrome(chrome_options=options)
        cls.driver.implicitly_wait(5)
        BasePage(cls.driver).visit_url()
        cls.token = BasePage(cls.driver).login_by_js(True)
        print(cls.token)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url(ReadConf().readconf("URL","cartURL"))

    # 已完成
    @get_screen_in_case_end_or_error
    def test_page_show(self):
        CartCheck(self.driver).check_cart_total_num(self.token)
        CartCheck(self.driver).check_cart_product_info(self.token)

    # def test_modify_num(self):
    #     pass
    #
    # def test_del_product(self):
    #     pass
    #
    # def test_multiple_del_product(self):
    #     pass
    #
    # 已完成
    @get_screen_in_case_end_or_error
    def test_product_detail(self):
        CartCheck(self.driver).check_goto_product_detail()
    #
    # def test_switch_sku(self):
    #     pass

    # 已完成
    def test_create_order(self):
        CartPage(self.driver).click_product_select_icon()
        CartPage(self.driver).click_create_order_btn()
        sleep(3)
        CartCheck(self.driver).check_create_order()


if __name__ == "__main__":
    unittest.main()

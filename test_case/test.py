from selenium import webdriver
import unittest
from BasePage import BasePage
from pages.cart_page import CartPage
from public.public import check_page
from selenium.webdriver.common.by import By



class HomeTest(unittest.TestCase,BasePage):


    # 搜索测试
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
        BasePage(self.driver).visit_url("https://emall.namektest.xyz/emall/pages/myCart/myCart?tenant=zjsyjt")





    def test_toast(self,expected=None):
        # CartPage(self.driver).click_create_order_btn()
        if self.assertTrue("404" in self.driver.page_source):
            unittest.TestCase().fail("404")
        else:
            toast=BasePage().get_toast()
            if toast==expected:
                print("出现符合预期的提示")
            else:
                print("出现非预期提示")


if __name__ == '__main__':
    unittest.main()








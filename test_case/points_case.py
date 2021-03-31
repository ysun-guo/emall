# coding:utf-8
from selenium import webdriver
import unittest
from public.BasePage import BasePage
from pages.points_page import PointsPage
from pages.home_page import HomePage
from public.readConf import ReadConf

from unittest import TestCase


class PointsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        return_list = BasePage(cls).class_setup_set(True)
        cls.driver = return_list[0]
        cls.token = return_list[1]

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        BasePage(self.driver).visit_url(ReadConf().readconf("URL", "pointsURL"))

    def test_points_info_check(self):
        '''
        积分明细页面成功展示
        '''
        print('**验证积分明细页面元素是否展示**')
        points_num_page = PointsPage(self.driver).get_points_num()
        point_item_1_page = PointsPage(self.driver).get_points_item_1_page()
        points_api = PointsPage(self.driver).get_point_item_1_api(self.token)
        points_num_api = points_api[0]
        points_item_1_api = points_api[1]
        BasePage(self.driver).assert_equal(points_num_page, points_num_api)
        TestCase().assertListEqual(point_item_1_page, points_item_1_api)

    def test_goto_saas(self):
        PointsPage(self.driver).click_saas_link()
        res = BasePage(self.driver).is_element_present(HomePage(self.driver)._saas_personal_info)
        if res is True:
            print('saas的个人信息页面已展示')
        else:
            TestCase().fail('saas页面个人信息模块未展示')
        BasePage(self.driver).check_exist_in_string('saash5', BasePage(self.driver).get_url())


if __name__ == '__main__':
    unittest.main()

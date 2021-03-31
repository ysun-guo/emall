# coding=utf-8

from public.BasePage import BasePage
from selenium.webdriver.common.by import By
from public.readConf import ReadConf
from public.operate_api import ReturnToken
import requests


class PointsPage(BasePage):
    # 元素定位信息
    _points_num = (By.CLASS_NAME, 'point-num')
    _saas_link = (By.CLASS_NAME, 'to-use')
    _points_list = (By.CLASS_NAME, 'point-list')
    _points_list_no_data =(By.CLASS_NAME, 'no-data')
    _points_list_have_data = (By.CLASS_NAME, 'point-item')
    _event_item= (By.CLASS_NAME, 'consume-order-code')
    _event_time = (By.CLASS_NAME, 'consume-dete')
    _event_point_changed = (By.CLASS_NAME, 'consume-point')


    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def click_saas_link(self):
        self.click_element(self._saas_link)

    def get_points_num(self):
        return self.get_element_value(self.find_element(self._points_num))

    def get_points_item_1_page(self):
        event_item_1 = self.get_element_value(self.find_elements(self._event_item)[0])
        event_time_1 = self.get_element_value(self.find_elements(self._event_time)[0])
        event_points_changed_1 = self.get_element_value(self.find_elements(self._event_point_changed)[0])
        point_item_1 = [event_item_1,event_time_1,event_points_changed_1]
        return point_item_1

    def get_point_item_1_api(self,token):
        host = ReadConf().readconf('HOST', 'host')
        tenant_id = ReadConf().readconf('Tenant', 'tenant_id')
        memberid = ReturnToken().return_member_info()[0]
        api = '/api/v1/member/'+str(memberid)+'/points/changed/list?startIndex=0&pageCount=1'
        url=host + api
        header = {
            "token": token,
            "tenantId": tenant_id
        }
        text = requests.get(url, headers=header)
        x = text.json()["body"]
        points_num = x["points"]
        points_num = '{:g}'.format(float(points_num))
        event_item_list = x["changedList"]["data"][0]
        event_item_1 = event_item_list["remark"]
        event_time_1 = event_item_list["created"]
        event_points_changed_1 = event_item_list["offset"]
        event_points_changed_1 = '{:g}'.format(float(event_points_changed_1))
        points_item_1_api = [event_item_1, event_time_1, str(event_points_changed_1)]
        return points_num, points_item_1_api





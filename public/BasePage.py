# encoding=utf-8

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from unittest import TestCase
from public.operate_api import ReturnToken
from public.readConf import ReadConf
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium import webdriver
import os


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 封装定位方式
    def find_element(self, *loc):
        try:
            return WebDriverWait(
                self.driver, 10, 0.5).until(
                ec.visibility_of_element_located(
                    *loc))
        except Exception as e:
            raise e

    def is_element_present(self, *loc):
        try:
            WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(*loc))
        except exceptions.TimeoutException:
            return False
        return True

    def is_show_toast(self):
        loc = (By.TAG_NAME, "uni-toast")
        flag = self.is_element_present(loc)
        print("是否有toast提示：" + str(flag))
        return flag

    def is_show_404(self):
        text = '404 Not Found'
        if text in self.driver.page_source:
            return True
        else:
            return False

    def find_elements(self, *loc):
        try:
            return WebDriverWait(self.driver, 10, 0.5).until(
                ec.visibility_of_any_elements_located(*loc))
        except Exception as e:
            raise e

    # 打开网址
    def visit_url(self, url=None):
        if url is None:
            url = ReadConf().readconf("URL", "homeURL")
        else:
            url = url
        self.driver.get(url)




    # 设置手机模式
    @staticmethod
    def device_dev_set():
        mobile_emulation = {"deviceName": "iPhone X"}
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_argument("--auto-open-devtools-for-tabs")
        return options

    def login_by_js(self, is_member):
        phone = ReadConf().readconf("PhoneNumber", "phone")
        tenant_code = ReadConf().readconf("Tenant", "tenant_code")
        if is_member:
            member_list = ReturnToken().return_member_info()
            member_id = member_list[0]
            token = member_list[1]
            self.driver.execute_script(
                "window.localStorage.setItem('namek_emall@"+tenant_code+"@token',JSON.stringify('" + token + "'))")
            self.driver.execute_script(
                "window.localStorage.setItem('namek_emall@"+tenant_code+"@member',JSON.stringify({id: '" + str(member_id) + "', phone: '" + phone + "'}))")
        else:
            token = ReturnToken().return_visit_token()
            self.driver.execute_script("window.localStorage.setItem('namek_emall@"+tenant_code+"@token',JSON.stringify('" + token + "'))")
        return token

    def class_setup_set(cls, status, flag = 1):
        if flag == 1:
            driver_path = os.getcwd() + '/chromedriver'
        else:
            driver_path = os.path.dirname(os.getcwd()) + '/chromedriver'
        options = BasePage(cls).device_dev_set()
        cls.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        cls.driver.implicitly_wait(5)
        BasePage(cls.driver).visit_url()
        cls.token = BasePage(cls.driver).login_by_js(status)
        return cls.driver, cls.token

    '''元素操作封装 '''
    # 点击元素
    def click_element(self, *loc):
        element = WebDriverWait(self.driver, 10, 0.5).until(ec.element_to_be_clickable(*loc))
        element.click()

    # 元素输入
    def sendkey_element(self, element, *values):
        element.send_keys(*values)

    # 获取元素的值
    def get_element_value(self, element):
        return element.text

    # 清空元素
    def clear_element(self, element):
        element.clear()

    # 获取某个元素的属性
    def get_element_attribute(self, element, attribute):
        return element.get_attribute(attribute)

    def get_url(self):
        return self.driver.current_url

    '''断言封装'''

    # 校验是否为真
    def assert_true(self, key):
        TestCase().assertTrue(key)

    # 校验是否为假
    def assert_false(self, key):
        TestCase().assertFalse(key)

    # 校验是否相等
    def assert_equal(self, key1, key2):
        TestCase().assertEqual(key1, key2)

    # 校验是否不相等
    def assert_not_equal(self, key1, key2):
        TestCase().assertNotEqual(key1, key2)

    # 校验页面是否存在某字符串
    def check_exist_in_page(self, text):
        self.assert_true(text in self.driver.page_source)

    # 校验字符串是否包含指定的字符串
    def check_exist_in_string(self, str1, str2):
        self.assert_true(str1 in str2)

    def get_toast_text(self):
        _toast_div = (By.TAG_NAME, 'uni-toast')
        ele = self.find_element(_toast_div)
        toast_text = self.get_element_value(ele)
        return toast_text

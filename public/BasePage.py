# encoding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from unittest import TestCase
from selenium.webdriver.chrome.options import Options
from operate_api import ReturnToken


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 封装定位方式
    def find_element(self, *loc):
        try:
            return WebDriverWait(
                self.driver, 10, 0.5).until(
                EC.visibility_of_element_located(
                    *loc))
        except Exception as e:
            raise e

    def find_elements(self, *loc):
        try:
            return WebDriverWait(self.driver, 10, 0.5).until(
                EC.visibility_of_any_elements_located(*loc))
        except Exception as e:
            raise e

    # 打开网址
    def visit_url(self, url=None):
        if url is None:
            url = 'https://emall.namektest.xyz/emall/?tenant=zjsyjt'
        else:
            url = url
        self.driver.get(url)
    # 设置手机模式

    def device_dev_set(self):
        mobile_emulation = {"deviceName": "iPhone 8"}
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.add_argument("--auto-open-devtools-for-tabs")
        self.driver.Chrome(chrome_options=options)

    def login_by_js(self, is_member, phone):
        if is_member:
            list = ReturnToken.return_member_info(phone)
            member_id = list[0]
            token = list[1]
            self.driver.execute_script(
                "window.localStorage.setItem('namek_emall@zjsyjt@token',JSON.stringify('" +
                token +
                "'))")
            self.driver.execute_script(
                "window.localStorage.setItem('namek_emall@zjsyjt@member',JSON.stringify({memberId: '" +
                str(member_id) +
                "', phone: '" +
                phone +
                "'}))")
        else:
            token = ReturnToken.return_visit_token()
            self.driver.execute_script(
                "window.localStorage.setItem('namek_emall@zjsyjt@token',JSON.stringify('" +
                token +
                "'))")
        return token
    # 切换iframe

    def switch_to_frame(self, id_or_name_or_element):
        self.driver.switch_to.frame(id_or_name_or_element)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    '''元素操作封装 '''

    # 点击元素
    def click_element(self, *loc):
        element = WebDriverWait(
            self.driver, 10, 0.5).until(
            EC.element_to_be_clickable(
                *loc))
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

    '''断言封装'''

    # 校验是否为真
    def assert_True(self, key):
        TestCase().assertTrue(key)

    # 校验是否为假
    def assert_False(self, key):
        TestCase().assertFalse(key)

    # 校验是否相等
    def assert_Equal(self, key1, key2):
        TestCase().assertEqual(key1, key2)

    # 校验是否不相等
    def assert_Not_Equal(self, key1, key2):
        TestCase().assertNotEqual(key1, key2)

    # 校验页面是否存在某字符串
    def check_exist_in_page(self, str):
        self.assert_True(str in self.driver.page_source)

    def check_exist_in_string(self, str1, str2):
        self.assert_True(str1 in str2)

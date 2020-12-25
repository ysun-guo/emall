# coding=utf-8
from HTMLReport import addImage
from unittest import TestCase
import logging

# 添加截图到报告中去
def get_screen_add_report(driver):
    image = driver.get_screenshot_as_base64()
    addImage(image)


# 截图装饰器
def get_screen_in_case_end_or_error(func):
    def f1(obj, *args, **kwargs):
        try:
            func(obj, *args, **kwargs)
            get_screen_add_report(obj.driver)
            # obj.driver.refresh()
        except BaseException:
            get_screen_add_report(obj.driver)
            # obj.driver.refresh()
            raise
    return f1


# 获取页面toast提示的装饰器
def check_page(func):
    def f1(obj, expected, *args, **kwargs):
        func(obj, expected, *args, **kwargs)
        if TestCase().assertTrue("404" in obj.driver.page_source):
            TestCase().fail("404")
        else:
            toast = obj.get_toast()
            if toast is None:
                logging.info("没有出现toast提示")
            else:
                if toast == expected:
                    logging.info("出现符合预期的提示:" + toast)
                else:
                    TestCase().fail("出现非预期提示:" + toast)
    return f1

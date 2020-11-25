# coding=utf-8
import time
import unittest
import HTMLReport
import os
import sys
import SMTL_upload
os.chdir(sys.path[0])

# 收集测试用例


def create_my_suit(flag):
    my_suit_smoke = unittest.TestSuite()
    my_suit = unittest.TestSuite()
    testdir = "test_case"
    discover = unittest.defaultTestLoader.discover(
        testdir, pattern="product_case.py", top_level_dir=None)
    for test_suit in discover:
        for test_cases in test_suit:
            my_suit.addTest(test_cases)
            for test_case in test_cases:
                test_case_name = test_case._testMethodName
                if test_case_name.startswith(
                        'test') and test_case_name.endswith('product_add_to_car'):
                    my_suit_smoke.addTest(test_case)
    if flag == 0:
        '''冒烟用例集'''
        return my_suit_smoke
    elif flag == 1:
        return my_suit


if __name__ == '__main__':
    mysuit = create_my_suit(0)
    now1 = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = now1
    runner = HTMLReport.TestRunner(report_file_name=filename,
                                   output_path='report',
                                   title='测试报告',
                                   description='emall测试环境的UI自动化结果',
                                   lang='cn'  # 支持中文与英文，默认中文
                                   )
    runner.run(mysuit)
    # 发送邮件
    # path='/Users/sy/PycharmProjects/emall/report/'+filename+'.html'
    # SMTL_upload.SendMail(path,filename)

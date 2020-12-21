# coding=utf-8
import time
import unittest
import HTMLReport
import os
import sys
import SMTL_upload
os.chdir(sys.path[0])

# 收集测试用例


def create_my_suit():
    # my_suit_smoke = unittest.TestSuite()
    # my_suit = unittest.TestSuite()
    test_dir = "test_case"
    discover = unittest.defaultTestLoader.discover(
        test_dir, pattern="*case.py", top_level_dir=None)
    # 冒烟用例集
    '''
    for test_file in discover:
        for test_cases in test_file:
            my_suit.addTest(test_cases)
            for test_case in test_cases:
                test_case_name = test_case._testMethodName
                if test_case_name.startswith(
                        'test') and test_case_name.endswith('product_add_to_car'):
                    my_suit_smoke.addTest(test_case)
    if flag == 0:
        return my_suit_smoke
    elif flag == 1:
        return discover
'''
    return discover


if __name__ == '__main__':
    my_suit = create_my_suit()
    now1 = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = now1
    runner = HTMLReport.TestRunner(report_file_name=filename,
                                   output_path='report',
                                   title='测试报告',
                                   description='emall测试环境的UI自动化结果',
                                   sequential_execution=True
                                   )
    runner.run(my_suit)
    # 发送邮件
    # path='/Users/sy/PycharmProjects/emall/report/'+filename+'.html'
    # SMTL_upload.SendMail(path,filename)

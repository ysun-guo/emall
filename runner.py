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
    test_dir = "test_case"
    discover = unittest.defaultTestLoader.discover(
        test_dir, pattern="*case.py", top_level_dir=None)
    return discover



if __name__ == '__main__':
    my_suit = create_my_suit()
    now1 = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = now1
    runner = HTMLReport.TestRunner(report_file_name=filename,
                                   output_path='report',
                                   title='测试报告',
                                   description='电商的UI自动化结果',
                                   sequential_execution=True
                                   )
    runner.run(my_suit)
    # 发送邮件
    report_path=os.getcwd()+'/report/'+filename+'.html'
    log_path=os.getcwd()+'/report/'+filename+'.log'
    SMTL_upload.SendMail(report_path, log_path, filename)

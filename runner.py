# coding=utf-8
from TestRunner.HTMLTestRunner import SMTP
from TestRunner.HTMLTestRunner import HTMLTestRunner
import logging
import time
import unittest
import os
import sys
os.chdir(sys.path[0])


def create_my_suit():
    test_dir = "test_case"
    discover = unittest.defaultTestLoader.discover(
        test_dir, pattern="*case.py", top_level_dir=None)
    return discover


if __name__ == '__main__':
    my_suit = create_my_suit()
    now1 = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = now1 + "_test_report.html"
    f = open("./report/" + filename, "wb")
    runner = HTMLTestRunner(
        verbosity=2, title='emallH5测试', stream=f
    )
    runner.run(my_suit)
    f.close()
    logging.info("运行结束！！开始邮件发送")
    # 发送邮件
    report_path = os.getcwd() + '/report/' + filename
    sender = 'suny@namek.com.cn'
    recevier = 'suny@namek.com.cn'
    password = '36aywwWhDjqokua8'
    host = 'imap.exmail.qq.com'
    subject = 'emallH5自动化结果'
    email = SMTP(recevier, password, host)
    email.sender(to=recevier, subject=subject, attachments=report_path)

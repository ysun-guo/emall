#coding=UTF-8

import os
import unittest
import requests
from public.BasePage import BasePage
from public.readConf import ReadConf

import datetime

class Tests(unittest.TestCase):
    def test_get_code_by_api(self):
        url=ReadConf().readconf('HOST', 'host')
        print(url)

if __name__ == '__main__':
    unittest.main()

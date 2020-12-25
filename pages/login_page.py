# coding:utf-8

from public.BasePage import BasePage
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class LoginPage(BasePage):

    _phone = (By.XPATH, '//input[@class=uni-input-input][1]')

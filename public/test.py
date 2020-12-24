
from readConf import ReadConf
import logging
import requests
import execjs
from readConf import ReadConf

host = ReadConf().readconf("HOST", "host")
api = '/api/v1/login/loginByPhone'
url = host + api

print(url)




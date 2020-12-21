
from readConf import ReadConf
import logging
import requests

api = '/api/v1/shopping/cart/num'
host = ReadConf().readconf("HOST", "host")
url = "http://47.97.206.135:8815/api/v1/shopping/cart/num"

header = {
    "token": "lRFBXp5GF9fhRgmWfg3xwUH87NMj0XyB",
    "tenantId": "100108"
}
req = requests.get(url, headers=header)
text = req.json()
print(text["body"])

import requests

import my_var

url = 'https://emall.namektest.xyz/api/v1/login/loginByPhone'
body = {
    "phone": '13175115726',
    "tenantId": 100134
}
s=requests.Session()
req1 = s.post(url, json=body)
text = req1.json()
token=(text['body']['token'])
print(req1.cookies)



api = '/api/v1/shopping/cart/list'
host = my_var.test_host
url = host + api
header = {
    "token": token,
    "tenantId": "100134"
}
req = requests.get(url, headers=header)
text = req.json()
texts=text["body"]
list=[]

for text in texts:
    body_text = text
    cart_id = body_text["id"]
    num = body_text["num"]
    product_name = body_text["product"]["name"]
    list.append([cart_id,num,product_name])

print(list)

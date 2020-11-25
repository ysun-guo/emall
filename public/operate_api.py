import requests

class ReturnToken():
    def return_visit_token(self):
        url = 'https://emall.namektest.xyz/api/v1/login/loginByAnonymous'
        data = {'tenantID': '100108', 'belongTenantId': '100108'}  # 请求数据
        req = requests.post(url, data)  # 发post请求
        text = req.json()  # 返回string,json串
        return text['body']['token']


    def return_member_info(self, phone="13175115726"):
        url = 'https://emall.namektest.xyz/api/v1/login/loginByPhone'
        body = {
        "phone": phone,
        "tenantId": 100108
        }
        req = requests.post(url, json=body)
        text = req.json()
        print(text)
        info_list = []
        info_list.append(text['body']['memberId'])
        info_list.append(text['body']['token'])
        return info_list

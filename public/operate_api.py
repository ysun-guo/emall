import requests
from readConf import ReadConf


class ReturnToken():

    def return_visit_token(self):
        tenantid = ReadConf().readconf("TenantID", "tenantid")
        host=ReadConf().readconf("HOST","host")
        api='/api/v1/login/loginByAnonymous'
        url = host+api
        data = {'tenantID': tenantid, 'belongTenantId': tenantid}  # 请求数据
        req = requests.post(url, data)  # 发post请求
        text = req.json()  # 返回string,json串
        return text['body']['token']

    def return_member_info(self):
        phone=ReadConf().readconf("PhoneNumber","phone")
        tenantid = ReadConf().readconf("TenantID", "tenantid")
        host=ReadConf().readconf("HOST","host")
        api='/api/v1/login/loginByPhone'
        url = host+api
        body = {
            "phone": phone,
            "tenantId": tenantid
        }
        req = requests.post(url, json=body)
        text = req.json()
        print(text)
        info_list = []
        info_list.append(text['body']['memberId'])
        info_list.append(text['body']['token'])
        return info_list

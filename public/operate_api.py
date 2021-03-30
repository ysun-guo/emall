import requests
from public.readConf import ReadConf


class ReturnToken():

    def return_visit_token(self):
        tenant_id = ReadConf().readconf("Tenant", "tenant_id")
        host = ReadConf().readconf("HOST", "host")
        api = '/api/v1/login/loginByAnonymous'
        url = host + api
        data = {'tenantID': tenant_id, 'belongTenantId': tenant_id}  # 请求数据
        req = requests.post(url, data)  # 发post请求
        text = req.json()  # 返回string,json串
        return text['body']['token']

    def return_member_info(self):
        phone = ReadConf().readconf("PhoneNumber", "phone")
        tenant_id = ReadConf().readconf("Tenant", "tenant_id")
        host = ReadConf().readconf("HOST", "host")
        api = '/api/v1/login/loginByPhone'
        url = host + api
        body = {
            "phone": phone,
            "tenantId": tenant_id
        }
        req = requests.post(url, json=body)
        text = req.json()
        info_list = []
        info_list.append(text['body']['memberId'])
        info_list.append(text['body']['token'])
        return info_list

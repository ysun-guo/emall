import requests
from public.readConf import ReadConf
import hashlib


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

    @staticmethod
    def create_md5(str1):
        md5 = hashlib.md5()
        md5.update(str1.encode('utf-8'))
        str1 = md5.hexdigest()
        return str1

    def return_saas_token_by_api(self):
        host = ReadConf().readconf('HOST', 'admin_host')
        api = '/api/v1/account/login'
        url = host+api
        user = ReadConf().readconf('AdminUser', 'adminuser')
        pwd = ReadConf().readconf('AdminUser', 'adminpwd')
        pwd = self.create_md5(pwd)
        body = {'tenantCode': 'namek', 'account': user, 'password': pwd}
        text = requests.post(url, data=body)
        saas_token = text.json()['body']['token']
        return saas_token
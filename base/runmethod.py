#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__: hunter


# import requests
# import json
#
# class RunMain:
#     def __init__(self, url, method, data=None):
#         self.t = self.run_main(url, method, data)
#
#     def send_post(self, url, data):
#         r = requests.post(url=url, data=json.dumps(data))
#         print(r.status_code)
#         result = r.json()
#         return json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)
#
#     def send_get(self, url, data):
#         r = requests.get(url=url, params=data)
#         result = r.json()
#         return json.dumps(result, indent=2, sort_keys=False, ensure_ascii=False)
#
#     def run_main(self, url, method, data=None):
#         if method == 'POST':
#             r = self.send_post(url=url,data=data)
#         else:
#             r = self.send_get(url=url, data=data)
#         return r
#
# if __name__ == "__main__":
#     url = 'http://192.168.0.157:18005/oauth/token'
#     data = {
#         'clientId': 'ut.usscity.com',
#         'password': '123456',
#         'userName': 'admin',
#         'VerificationCode': '',
#         'VerificationCodeKey': "f7dc3967-bfbc-4a0f-9e2d-4d6e403d10a1"
#     }
#     test = RunMain(url, 'POST', data)
#     print(test.t)




import requests
import json


class RunMain:
    def send_get(self, url, data):
        res = requests.get(url=url, params=data).json()
        # return res
        return json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False)

    def send_post(self, url, data):
        res = requests.post(url=url, data=json.dumps(data)).json()
        # return res
        return json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False)

    def run_main(self, url, method, data=None):
        if method == 'POST':
            res = self.send_post(url, data)
        else:
            res = self.send_get(url, data)
        return res


if __name__ == "__main__":
    url = 'http://192.168.0.157:18005/oauth/token'
    data = {
        'clientId': 'ut.usscity.com',
        'password': '123456',
        'userName': 'admin',
        'VerificationCode': '',
        'VerificationCodeKey': "f7dc3967-bfbc-4a0f-9e2d-4d6e403d10a1"
    }
    test = RunMain()
    print(test.run_main(url, 'POST', data))

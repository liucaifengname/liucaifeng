# _*_ coding:utf-8 _*_
import requests
import unittest
import json

class Test_login(unittest.TestCase):

    url='https://passport.womai.com/login/login.do'

    headers={"Accept": "application/json, text/javascript, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "161",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "passport.womai.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "X-Requested - With":"XMLHttpRequest"
             }

    pyload={"serverPath":" http://www.womai.com/",
            "loginId": "liucaifeng666",
            "password": "liucaifeng666",
            "validateCode":"",
            "tempcode":"",
            "mid":" 0",
            "returnUrl":"http://www.womai.com/index-31000-0.htm"
            }

    def test_login(self):

        response=requests.post(self.url,headers=self.headers,data=self.pyload)
        json_data=response.json()
        print(json_data)
        #
        self.assertEqual('2',json_data['msg'])


if __name__ == '__main__':
    unittest.main()













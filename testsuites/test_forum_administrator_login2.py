# _*_ coding:utf-8 _*_
from luntan.testsuites.base_testcase import BaseTestCase
from luntan.pageobjects.forum_administrator_homepage2 import  HomePage
import unittest
import time

class BaiduSearch(BaseTestCase):
    def test_forum_login(self):
        forum_homepage=HomePage(self.driver)
        time.sleep(3)
        forum_homepage.login('admin', 'password','password','haotest','haotest','：北京haotest科技','web应用安全',
                             '渗透，免杀，逆向，脱壳，破解，漏洞，攻防，安全','好好学习，fighting!fighting')
if __name__ == '__main__':
    unittest.main()

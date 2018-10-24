# _*_ coding:utf-8 _*_
from luntan.testsuites.base_testcase import BaseTestCase
from luntan.pageobjects.forum_administrator_homepage4 import  HomePage
import unittest
import time

class BaiduSearch(BaseTestCase):
    def test_forum_login(self):
        forum_homepage=HomePage(self.driver)
        time.sleep(3)
        forum_homepage.login('admin', 'password','安勇是不是天底下最帅的大帅哥？','是','不是')
if __name__ == '__main__':
    unittest.main()

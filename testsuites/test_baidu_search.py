from baidu.testsuites.base_testcase import BaseTestCase
from baidu.pageobjects.baidu_homepage import HomePage
import unittest
import time

class BaiduSearch(BaseTestCase):

    def test_baidu_search(self):

        home_page=HomePage(self.driver)
        # home_page.open_url('http://www.baidu.com')
        home_page.search('selenium')
        time.sleep(3)
if __name__ == '__main__':
    unittest.main()

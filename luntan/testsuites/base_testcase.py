from selenium import webdriver
from  luntan.framework.browser_engine import BrowserEngine
import unittest
import time



class BaseTestCase(unittest.TestCase):

    def setUp(self):#测试提前准备工作
        browser=BrowserEngine()
        self.driver=browser.open_browser()

    def tearDown(self):#主要是测试结束后要做的工作
        self.driver.quit()

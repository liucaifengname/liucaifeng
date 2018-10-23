#-*-coding:utf-8 -*-
import os.path
from configparser import ConfigParser
from  selenium import webdriver
from luntan.framework.logger import  Logger



logger=Logger(logger='BrowserEngine').getlog()

class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath('.')) #注意相对路径获取方法
    chrome_driver_path=dir + '/tools/chromedriver.exe'

    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser=config.get('browserType','browserName')
        logger.info('You had select %s browser.' % browser)
        url=config.get('testServer','URL')
        logger.info('The  test server url is: %s' % url)

        # if browser == 'Firefox':
        #     driver=webdriver.Firefox()
        #     logger.info('Starting firefox browser.')
        if browser == 'Chrome':
            driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info('启动了Chrome浏览器')

        driver.get(url)
        logger.info('Open url :%s'% url)
        driver.maximize_window()
        logger.info('maximize the current window.窗口最大化')
        driver.implicitly_wait(10)
        logger.info('Set implicitly wait 10 seconds.隐式等待10秒')
        return driver

    def quit_browser(self):
        self.driver.quit()
        logger.info('Now,Close and quit the browser.')







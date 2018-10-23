from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from luntan.framework.logger import Logger
import time
import os.path

logger=Logger(logger='BasePage').getlog()

class BasePage(object):

    def __init__(self,driver):
        self.driver=driver
    #返回
    def back(self):
        self.driver.back()
        logger.info('Click back on current page.')
    #前进
    def forward(self):
        self.driver.forward()
        logger.info('Click forward on current page.')
    # 浏览器打开一个页面
    def open_url(self, url):
        self.driver.get(url)
        logger.info('Click open_url on current page.')
    # 关闭浏览器
    def close(self):
        try:
            self.driver.close()
            logger.info('Closing and quit the browser.')
        except Exception as e:
            logger.error('Failed to quit the browaer with %s' % e)

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))

            return self.driver.find_element(*loc)
            logger.info('找到页面元素-->', loc)

        except:
            logger.info("页面未能找到",(self, loc))
            logger.info('%s 页面中未找到 %s 元素' %(self,loc))

    # 保存图片
    def get_windows_img(self,*loc):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 全路径
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('Had takescreenshot and save to folder :/screenshots')
        except Exception as e:
            logger.info('页面未找到', (self,*loc))
            logger.info('Failed to take screenshot! %s' %e)
    # 输入
    def sendkeys(self,text,*loc):
        element = self.find_element(*loc)
        # element.clear()
        try:
            element.send_keys(text)
        except:
            logger.info('页面未找到', (self, loc))
    # 清除文本框
    def clear(self,*loc):
        element = self.find_element(*loc)
        try:
            element.clear()
        except Exception as e:
            logger.info('页面未找到', (self, loc))

    # 点击元素
    def click(self,*loc):
        element = self.find_element(*loc)
        try:
            element.click()
        except Exception as e:
            logger.info("Faild to click the element with %s" ,e)
    # 激活当前窗口
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        window_list = self.driver.current_window_handle
        self.driver.switch_to.window(window_list)
        logger.info('当前窗口已被激活')
    def switch_to_window1(self):
        self.driver.switch_to.window(self.driver.window_handles[2])
        window_list = self.driver.current_window_handle
        self.driver.switch_to.window(window_list)

    #关闭当前窗口
    def close_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        window_list = self.driver.current_window_handle
        self.driver.switch_to.window(window_list)
        logger.info('当前窗口已被关闭')

    def close_window1(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        window_list = self.driver.current_window_handle
        self.driver.switch_to.window(window_list)

    def switch_to_iframe(self):
        self.driver.switch_to.frame('main')

    def find(self,*loc):
        element=self.driver.find_element(*loc)
        logger.info('%s'%element.text)


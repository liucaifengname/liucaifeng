from luntan.pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
from luntan.framework.logger import Logger


logger=Logger(logger='HomePage').getlog()
class HomePage(BasePage):

    # 查找元素，进行登录
    forum_homepage_input_input_loc = (By.ID, 'ls_username')
    forum_homepage_password_input_loc = (By.ID, 'ls_password')
    forum_homepage_button_input_loc = (By.CSS_SELECTOR, '.y tr:last-child .fastlg_l')


    # 开始进行帖子搜索，搜索haotest帖子
    forum_homepage_search_input_loc = (By.CSS_SELECTOR, '#scbar_txt')
    forum_homepage_click_input_loc = (By.CSS_SELECTOR, '#scbar_btn')
    forum_homepage_into_input_loc = (By.CSS_SELECTOR, '.xs3 font')

    # 用户退出
    forum_homepage_exit_input_loc = (By.CSS_SELECTOR, '#hd #um p> *:last-child')

    def login(self, username, password,search):
        #登录
        self.sendkeys(username, *self.forum_homepage_input_input_loc)
        self.sendkeys(password, *self.forum_homepage_password_input_loc)
        self.click(*self.forum_homepage_button_input_loc)
        time.sleep(2)
        logger.info('用户登录成功')

        #搜索
        self.sendkeys(search,*self.forum_homepage_search_input_loc)
        time.sleep(2)
        self.click(*self.forum_homepage_click_input_loc)
        logger.info('搜索haotest帖子')

        time.sleep(1)
        self.switch_to_window()
        time.sleep(2)
        self.click(*self.forum_homepage_into_input_loc)
        logger.info('点击进入haotest帖子')
        time.sleep(1)
        self.switch_to_window1()
        time.sleep(3)
        self.close_window1()
        time.sleep(1)
        self.close_window()

        #退出
        time.sleep(3)
        self.click(*self.forum_homepage_exit_input_loc)
        logger.info('用户退出登录')

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


    # 开始进入默认板块
    forum_homepage_default_input_loc = (By.CSS_SELECTOR, '.bm_c tr:first-child td a')

    # 发帖
    forum_homepage_TextTitle_input_loc = (By.CSS_SELECTOR, '.pbt #subject')
    forum_homepage_TextBox_input_loc = (By.CSS_SELECTOR, '.area #fastpostmessage')
    forum_homepage_submit_input_loc = (By.CSS_SELECTOR, '.bm_c #fastpostform p .pn')

    # 回帖
    forum_homepage_reply_input_loc = (By.CSS_SELECTOR, '.area #fastpostmessage')
    forum_homepage_PublishReply_input_loc = (By.CSS_SELECTOR, '.pl tr td:last-child .pn')

    # 用户退出
    forum_homepage_exit_input_loc = (By.CSS_SELECTOR, '#hd #um p> *:last-child')

    def login(self, username, password, title, content, reply):
        #登录
        self.sendkeys(username, *self.forum_homepage_input_input_loc)
        time.sleep(2)
        self.sendkeys(password, *self.forum_homepage_password_input_loc)
        self.click(*self.forum_homepage_button_input_loc)
        logger.info('普通用户登录成功')
        time.sleep(3)
        #默认
        self.click(*self.forum_homepage_default_input_loc)
        logger.info('进入默认模块')
        time.sleep(3)
        #发表
        self.sendkeys(title, *self.forum_homepage_TextTitle_input_loc)
        time.sleep(2)
        self.sendkeys(content, *self.forum_homepage_TextBox_input_loc)
        time.sleep(2)
        self.click(*self.forum_homepage_submit_input_loc)
        logger.info('点击发表帖子')
        time.sleep(3)
        #回复
        self.sendkeys(reply, *self.forum_homepage_reply_input_loc)
        time.sleep(3)
        self.click(*self.forum_homepage_PublishReply_input_loc)
        logger.info('回帖成功')
        #退出
        time.sleep(3)
        self.click(*self.forum_homepage_exit_input_loc)
        logger.info('用户退出登录')

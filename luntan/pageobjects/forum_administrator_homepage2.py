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

    ## delete板块
    forum_homepage_delete1_input_loc = (By.CSS_SELECTOR, '.bm_c tr:first-child .o')
    forum_homepage_delete2_input_loc = (By.CSS_SELECTOR, '.o input')
    forum_homepage_delete3_input_loc = (By.CSS_SELECTOR, '#mdly p a')
    forum_homepage_delete4_input_loc = (By.CSS_SELECTOR, '#modsubmit')

    # #进入版块管理(管理中心--论坛)
    forum_homepage_center_input_loc = (By.CSS_SELECTOR, '#hd #um p> *:nth-last-child(3)')
    forum_homepage_password1_input_loc = (By.CSS_SELECTOR, '#loginform p:nth-last-child(6) .txt')
    forum_homepage_submit_input_loc = (By.CSS_SELECTOR, '.btn')
    forum_homepage_forum_input_loc = (By.CSS_SELECTOR, '#topmenu li:nth-last-child(8) a')

    #添加新版块
    forum_homepage_tianjia_input_loc = (By.CSS_SELECTOR, '.lastboard a')
    forum_homepage_input1_input_loc = (By.CSS_SELECTOR, '.tb tbody:nth-last-child(2) tr:nth-last-child(2) td:last-child .txt')
    forum_homepage_submit1_input_loc = (By.CSS_SELECTOR, '.fixsel .btn')

    #退出管理中心
    forum_homepage_quit_input_loc = (By.CSS_SELECTOR, '#frameuinfo a')

    #进入论坛
    forum_homepage_forum1_input_loc = (By.CSS_SELECTOR, '.z a:nth-child(3)')
    # 管理员退出
    forum_homepage_exit_input_loc = (By.CSS_SELECTOR, '#um p >*:last-child')

    # 查找元素，普通员工进行登录
    forum_homepage_input2_input_loc = (By.ID, 'ls_username')
    forum_homepage_password2_input_loc = (By.ID, 'ls_password')
    forum_homepage_button2_input_loc = (By.CSS_SELECTOR, '.y tr:last-child .fastlg_l')

    # 开始进入新板块
    forum_homepage_new_input_loc = (By.CSS_SELECTOR, '.bm_c tr:nth-last-child(2) td')

    # 发帖
    forum_homepage_TextTitle_input_loc = (By.CSS_SELECTOR, '.pbt #subject')
    forum_homepage_TextBox_input_loc = (By.CSS_SELECTOR, '.area #fastpostmessage')
    forum_homepage_submit2_input_loc = (By.CSS_SELECTOR, '.bm_c #fastpostform p .pn')

    # 回帖
    forum_homepage_reply_input_loc = (By.CSS_SELECTOR, '.area #fastpostmessage')
    forum_homepage_PublishReply_input_loc = (By.CSS_SELECTOR, '.pl tr td:last-child .pn')

    def login(self, username, password,password1,username2, password2,new,title, content, reply):
        #登录
        self.sendkeys(username, *self.forum_homepage_input_input_loc)
        time.sleep(2)
        self.sendkeys(password, *self.forum_homepage_password_input_loc)
        self.click(*self.forum_homepage_button_input_loc)
        logger.info('管理员登录成功')
        time.sleep(3)
        #默认
        self.click(*self.forum_homepage_default_input_loc)
        logger.info('进入默认模块')
        time.sleep(2)
        # 删除帖子
        self.click(*self.forum_homepage_delete1_input_loc)
        time.sleep(2)
        self.click(*self.forum_homepage_delete2_input_loc)
        time.sleep(2)
        self.click(*self.forum_homepage_delete3_input_loc)
        time.sleep(2)
        self.click(*self.forum_homepage_delete4_input_loc)
        logger.info('删除帖子成功')

        # #进入版块管理(管理中心--论坛)
        self.click(*self.forum_homepage_center_input_loc)
        time.sleep(2)
        self.switch_to_window()

        self.sendkeys(password1, *self.forum_homepage_password1_input_loc)
        time.sleep(2)
        self.click(*self.forum_homepage_submit_input_loc)
        logger.info('登录管理中心')
        time.sleep(2)
        self.click(*self.forum_homepage_forum_input_loc)
        logger.info('进入论坛')
        time.sleep(2)
        self.switch_to_iframe()

        time.sleep(5)
        self.click(*self.forum_homepage_tianjia_input_loc)
        time.sleep(2)
        self.sendkeys(new, *self.forum_homepage_input1_input_loc)
        time.sleep(2)
        self.click(*self.forum_homepage_submit1_input_loc)
        logger.info('添加新版块成功')
        #退出管理员中心
        time.sleep(2)
        self.click(*self.forum_homepage_quit_input_loc)
        logger.info('退出管理员中心')
        time.sleep(2)
        self.close_window()

        time.sleep(2)
        self.click(*self.forum_homepage_forum1_input_loc)
        logger.info('点击论坛')
        time.sleep(3)
        self.click(*self.forum_homepage_exit_input_loc)
        time.sleep(2)
        logger.info('管理员退出登录')

        # 普通员工登录
        self.sendkeys(username2, *self.forum_homepage_input_input_loc)
        time.sleep(2)
        self.sendkeys(password2, *self.forum_homepage_password_input_loc)
        self.click(*self.forum_homepage_button_input_loc)
        time.sleep(3)
        logger.info('普通员工登录成功')
        # 进入新版块
        self.click(*self.forum_homepage_new_input_loc)
        time.sleep(3)
        logger.info('进入新版块成功')
        # 发表
        self.sendkeys(title, *self.forum_homepage_TextTitle_input_loc)
        time.sleep(2)
        self.sendkeys(content, *self.forum_homepage_TextBox_input_loc)
        time.sleep(2)
        self.click(*self.forum_homepage_submit2_input_loc)
        time.sleep(3)
        logger.info('普通用户发表帖子成功')
        # 回复
        self.sendkeys(reply, *self.forum_homepage_reply_input_loc)
        time.sleep(3)
        self.click(*self.forum_homepage_PublishReply_input_loc)
        logger.info('普通用户回帖成功')
        #退出
        time.sleep(3)
        self.click(*self.forum_homepage_exit_input_loc)
        logger.info('普通用户退出登录')




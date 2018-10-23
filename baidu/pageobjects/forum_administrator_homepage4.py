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

    #发表投票帖子
    forum_homepage_post_input_loc = (By.CSS_SELECTOR, '#newspecial')
    forum_homepage_vote_input_loc = (By.CSS_SELECTOR, '#editorbox li:last-child a')

    forum_homepage_title_input_loc = (By.CSS_SELECTOR, '.pbt span:first-child input')

    forum_homepage_option1_input_loc = (By.CSS_SELECTOR, '#pollm_c_1 p:nth-child(1) input')
    forum_homepage_option2_input_loc = (By.CSS_SELECTOR, '#pollm_c_1 p:nth-child(2) input')
    forum_homepage_option3_input_loc = (By.CSS_SELECTOR, '.mtm span')

    #进行投票
    forum_homepage_optionStart_input_loc = (By.CSS_SELECTOR, '#option_1')
    forum_homepage_submit_input_loc = (By.CSS_SELECTOR, '#pollsubmit span')

    forum_homepage_title1_input_loc = (By.CSS_SELECTOR, '.ts span')
    forum_homepage_option_1_input_loc = (By.CSS_SELECTOR, '#poll .pcht tr:first-child label')
    forum_homepage_option_2_input_loc = (By.CSS_SELECTOR, '#poll .pcht tr:nth-child(3) label')
    forum_homepage_option_1_data_input_loc = (By.CSS_SELECTOR, '.pcht tr:nth-child(2) td:last-child')
    forum_homepage_option_2_data_input_loc = (By.CSS_SELECTOR, '.pcht tr:nth-child(4) td:last-child')

    # 管理员退出
    forum_homepage_exit_input_loc = (By.CSS_SELECTOR, '#um p >*:last-child')

    def login(self, username, password,title,option1,option2):
        #登录
        self.sendkeys(username, *self.forum_homepage_input_input_loc)
        self.sendkeys(password, *self.forum_homepage_password_input_loc)
        self.click(*self.forum_homepage_button_input_loc)
        logger.info('登录成功')
        time.sleep(2)
        #默认
        self.click(*self.forum_homepage_default_input_loc)
        logger.info('进入默认模块成功')
        time.sleep(3)

        #投票帖子
        self.click(*self.forum_homepage_post_input_loc)
        logger.info('点击发帖')
        time.sleep(2)
        self.click(*self.forum_homepage_vote_input_loc)
        logger.info('选择发帖投票')
        time.sleep(2)
        self.sendkeys(title, *self.forum_homepage_title_input_loc)
        time.sleep(2)
        self.sendkeys(option1, *self.forum_homepage_option1_input_loc)
        time.sleep(2)
        self.sendkeys(option2, *self.forum_homepage_option2_input_loc)
        time.sleep(2)
        self.click(*self.forum_homepage_option3_input_loc)
        logger.info('点击发起投票')

        #开始投票
        time.sleep(2)
        self.click(*self.forum_homepage_optionStart_input_loc)
        logger.info('选择投票选项')
        time.sleep(2)
        self.click(*self.forum_homepage_submit_input_loc)
        logger.info('提交投票成功')
        #退出

        self.find(*self.forum_homepage_title1_input_loc,)
        self.find(*self.forum_homepage_option_1_input_loc)
        self.find(*self.forum_homepage_option_2_input_loc)
        self.find(*self.forum_homepage_option_1_data_input_loc)
        self.find(*self.forum_homepage_option_2_data_input_loc)

        time.sleep(5)
        self.click(*self.forum_homepage_exit_input_loc)
        logger.info('点击退出')






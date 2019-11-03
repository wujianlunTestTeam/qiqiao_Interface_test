#登录界面

from page_obj.page import Page
from pubilc.driver import pcdriver


class LoginPage(Page):
    '''登录界面'''

    login_url = 'https://qy.do1.com.cn/qiqiao/runtime'
    denglu = "//a[text()='账号密码登录']"
    zhanghao = "//input[@title='请输入账号']"
    mima = "//input[@title='请输入密码']"
    anniu = "//button[text()='登录']"







    # 定义统一登录入口
    def user_login(self, username,password):
        '''通过用户名密码登录'''
        self.open(self.login_url)
        self.find_elem_is_clickableByXPATH(self.denglu).click()
        self.find_elem_visibleByXPATH(self.zhanghao).send_keys(username)
        self.find_elem_visibleByXPATH(self.mima).send_keys(password)
        self.find_elem_is_clickableByXPATH(self.anniu).click()


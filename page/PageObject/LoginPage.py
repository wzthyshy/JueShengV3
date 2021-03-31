"""
-----------------------------
@Time : 2021/03/25 21:40
@Auth : Wang
@File : LoginPage.py
@IDE  : Pycharm
-----------------------------
注：封装登录页面的元素
"""

from JueShengV3.config.parseConfile import ParseConFile
from JueShengV3.page.BaePage import BasePage


class LoginPage(BasePage):
    # 读取配置表中的信息
    read_conf = ParseConFile()
    # 获取输入用户名的定位方法与名称
    username = read_conf.get_locator_or_options('LoginPageElements', 'username')
    # 获取输入密码框的定位方法与名称
    password = read_conf.get_locator_or_options('LoginPageElements', 'password')
    # 获取登录按钮的定位方法与名称
    loginBtn = read_conf.get_locator_or_options('LoginPageElements', 'loginBtn')
    # 获取登录失败弹出信息的定位方法与名称
    error_login = read_conf.get_locator_or_options('', '')
    # 获取登录成功的验证信息的定位方法与名称
    success_login = read_conf.get_locator_or_options('HomePageElements', 'loginmessge')

    def login(self, username, password):
        """登录流程"""
        self.open_url()
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()

    def open_url(self):
        return self.load_url('url')

    def clear_username(self):
        return self.clear(*LoginPage.username)

    def input_username(self, username):
        self.clear_username()
        return self.send_keys(*LoginPage.username, username)

    def clear_password(self):
        return self.clear(*LoginPage.password)

    def input_password(self, password):
        self.clear_password()
        return self.send_keys(*LoginPage.password, password)

    def click_login_btn(self):
        return self.click(*LoginPage.loginBtn)

    def get_error_login(self):
        return self.get_element_text(*LoginPage.error_login)

    def get_login_success_account(self):
        return self.get_element_text(*LoginPage.success_login)


if __name__ == "__main__":
    pass

"""
-----------------------------
@Time : 2021/03/25 21:40
@Auth : Wang
@File : LoginPage.py
@IDE  : Pycharm
-----------------------------
注：封装登录页面的元素
"""
from JueShengV3.Js_element import CssElement
from JueShengV3.config.parseConfile import ParseConFile
from JueShengV3.page.BasePage import BasePage


class LoginPage(BasePage):
    # 读取配置表中的信息
    read_conf = ParseConFile()
    # 获取输入用户名的定位方法与名称
    username = read_conf.get_locator_or_options('LoginPageElements', 'username')
    # 获取输入密码框的定位方法与名称
    password = read_conf.get_locator_or_options('LoginPageElements', 'password')
    # 获取输入验证码框的定位方法与名称
    code = read_conf.get_locator_or_options('LoginPageElements', 'code')
    # 获取登录按钮的定位方法与名称
    loginBtn = read_conf.get_locator_or_options('LoginPageElements', 'loginBtn')
    # 获取登录失败弹出信息的定位方法与名称
    error_login = read_conf.get_locator_or_options('LoginPageElements', 'error_login')
    # 获取登录成功的验证信息的定位方法与名称
    success_login = read_conf.get_locator_or_options('HomePageElements', 'success_login_msg')
    url = read_conf.get_locator_or_options('V3LoginAccount', 'url')

    def login(self, username, password, code):
        """登录流程"""
        self.load_url(*LoginPage.url)
        self.clear(*LoginPage.username)
        self.send_keys(*LoginPage.username, username)
        self.clear(*LoginPage.password)
        self.send_keys(*LoginPage.password, password)
        self.clear(*LoginPage.code)
        self.send_keys(*LoginPage.code, code)
        self.click(*LoginPage.loginBtn)

    def get_error_login(self):
        element = CssElement("#to-recover", describe="登录")
        element.click()
        return self.get_element_text(*LoginPage.error_login)

    def get_login_success_account(self):
        return self.get_element_text(*LoginPage.success_login)


if __name__ == "__main__":
    pass

"""
-----------------------------
@Time : 2021/03/25 21:40
@Auth : Wang
@File : test_login_case.py
@IDE  : Pycharm
-----------------------------
注：封装登录页面的操作逻辑
"""

import pytest

from JueShengV3.data.login_data import LoginData
from JueShengV3.page.PageObject.LoginPage import LoginPage


class TestLogin(object):
    """登录"""
    login_data = LoginData

    @pytest.mark.parametrize('username, password, code', login_data.login_success_data)
    def test_login(self,  username, password, code):
        login_page = LoginPage()
        login_page.login(username, password, code)
        actual = login_page.get_login_success_account()
        assert username in actual, "登录成功, 断言成功"

    @pytest.mark.parametrize('username, password, code, expect', login_data.login_fail_data)
    def test_fail(self,  username, password, code, expect):
        login_page = LoginPage()
        login_page.login(username, password, code)
        actual = login_page.get_error_login()
        assert actual == expect, "登录失败, 断言失败"


if __name__ == "__main__":
    pytest.main(['-v', 'test_loginCase.py'])

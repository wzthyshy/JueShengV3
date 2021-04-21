import pytest
from JueShengV3.page.PageObject.LoginPage import LoginPage
from JueShengV3.config.parseConfile import ParseConFile

do_conf = ParseConFile()
# 从配置文件中获取正确的用户名和密码
userName = do_conf.get_locator_or_options('V3LoginAccount', 'username')
passWord = do_conf.get_locator_or_options('V3LoginAccount', 'password')
code = do_conf.get_locator_or_options('V3LoginAccount', 'code')


@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = LoginPage(driver)
    yield driver, login_page


# @pytest.fixture(scope='function')
# def open_url(ini_pages):
#     login_page = ini_pages[1]
#     print(login_page)
#
#     yield login_page




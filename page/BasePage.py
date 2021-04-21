"""
-----------------------------
@Time : 2021/03/25 21:40
@Auth : Wang
@File : BasePage.py
@IDE  : Pycharm
-----------------------------
注：封装一些selenium操作
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
    NoAlertPresentException,
)

from JueShengV3.Js_element import CssElement


class BasePage(object):
    driver = webdriver.Chrome

    def __init__(self, driver, url, timeout=30):
        self.driver = driver
        self.url = url
        self.outTime = timeout
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT,
            'css': By.CSS_SELECTOR
        }
        # 创建字典，用于存放定位元素的所有方法

    def find_element(self, by, locator):
        """
        判断超时
        find alone element
        :param by: eg: id, name, xpath, css.....
        :param locator: id, name, xpath for str
        :return: element object
        """

        try:
            print('[Info:Starting find the element "{}" by "{}"!]'.format(locator, by))
            element = WD(self.driver, self.outTime).until(lambda x: x.find_element(by, locator))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(locator), t)
        else:
            return element

    def find_elements(self, by, locator):
        """
        判断超时
        find group elements
        :return: elements object
        """
        try:
            print('[Info:start find the elements "{}" by "{}"!]'.format(locator, by))
            elements = WD(self.driver, self.outTime).until(lambda x: x.find_elements(by, locator))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(locator), t)
        else:
            return elements

    def is_element_exist(self, by, locator):
        """
        判断元素是否存在
        assert element if exist
        :return: if element return True else return false
        """
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime). \
                    until(ec.visibility_of_element_located((self.byDic[by], locator)))
            except TimeoutException:
                print('Error: element "{}" not exist'.format(locator))
                return False
            return True
        else:
            print('the "{}" error!'.format(by))

    def is_click(self, by, locator):
        """
        判断元素是否可点击
        """
        if by.lower() in self.byDic:
            try:
                element = WD(self.driver, self.outTime). \
                    until(ec.element_to_be_clickable((self.byDic[by], locator)))
            except TimeoutException:
                print("元素不可以点击")
            else:
                return element
        else:
            print('the "{}" error!'.format(by))

    def is_alert(self):
        """
        判断是否存在弹出提示
        assert alert if exsit
        """
        try:
            re = WD(self.driver, self.outTime).until(ec.alert_is_present())
        except (TimeoutException, NoAlertPresentException):
            print("error:no found alert")
        else:
            return re

    def switch_to_frame(self, by, locator):
        """判断frame是否存在，存在就跳到frame"""
        print('info:switching to iframe "{}"'.format(locator))
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime). \
                    until(ec.frame_to_be_available_and_switch_to_it((self.byDic[by], locator)))
            except TimeoutException as t:
                print('error: found "{}" timeout！切换frame失败'.format(locator), t)
        else:
            print('the "{}" error!'.format(by))

    def switch_to_default_frame(self):
        """返回默认的frame"""
        print('info:switch back to default iframe')
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(e)

    def get_alert_text(self):
        """获取alert的提示信息"""
        alert = self.is_alert()
        if alert:
            return alert.text
        else:
            return None

    def get_element_text(self, by, locator, name=None):
        """获取某一个元素的text信息"""
        try:
            element = self.find_element(by, locator)
            if name:
                return element.get_attribute(name)
            else:
                return element.text
        except AttributeError:
            print('get "{}" text failed return None'.format(locator))

    def load_url(self, url):
        """加载url"""
        print('info: string upload url "{}"'.format(url))
        self.driver.get(url)

    def send_keys(self, by, locator, value=''):
        """写数据"""
        print('info:input "{}"'.format(value))
        try:
            element = self.find_element(by, locator)
            element.send_keys(value)
        except AttributeError as e:
            print(e)

    def clear(self, by, locator):
        """清理数据"""
        print('info:clearing value')
        try:
            element = self.find_element(by, locator)
            element.clear()
        except AttributeError as e:
            print(e)

    def click(self, by, locator):
        """点击某个元素"""
        print('info:click "{}"'.format(locator))
        element = self.is_click(by, locator)
        if element:
            element.click()
        else:
            print('the "{}" unclickable!')

    @staticmethod
    def js_element(self):

        element = CssElement("#to-recover", describe="登录")
        element.click()

    def open(self):
        self.driver.get(self.url)

    # 关闭浏览器，释放资源
    def quit(self):
        sleep(4)
        self.driver.quit()


if __name__ == "__main__":
    pass

from selenium.webdriver.common.by import By

from JueShengV3.config.parseConfile import ParseConFile
from JueShengV3.page.BasePage import BasePage


class MainPage(BasePage):
    # 获取配置表的信息
    read_conf = ParseConFile()
    # 获取关闭弹出框的定位方法与名称
    closetiplog = read_conf.get_locator_or_options('HomePageElements', 'closetiplog')

    loadtodo = read_conf.get_locator_or_options('HomePageElements', 'waitproc')
    todolist = read_conf.get_locator_or_options('HomePageElements', 'wanttodo')

    def close_arlt_text(self):
        return self.click(*MainPage.closetiplog)

    def goto_loadtodo(self, load):
        return self.click(*MainPage.loadtodo)

    def go_to_myform(self):
        return FormPage()


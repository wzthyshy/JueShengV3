class CssElement(object):

    driver = None

    def __init__(self, css, index=None, describe=None):
        self.css = css
        if index is None:
            self.index = 0
        else:
            self.index = index
        self.desc = describe

    def __get__(self, instance, owner):
        if instance is None:
            return None
        global driver
        driver = instance.driver
        return self

    def clear(self):
        """
        清除内容
        """
        js = """var elm = document.querySelectorAll("{css}")[{index}];
                    elm.style.border="2px solid red";
                    elm.value = "";""".format(css=self.css, index=self.index)
        driver.execute_script(js)

    def input(self, value):
        """
        输入内容
        """
        js = """var elm = document.querySelectorAll("{css}")[{index}];
                    elm.style.border="2px solid red";
                    elm.value = "{value}";""".format(css=self.css, index=self.index, value=value)
        driver.execute_script(js)

    def click(self):
        """
        点击元素
        """
        js = """var elm = document.querySelectorAll("{css}")[{index}];
                   elm.style.border="2px solid red";
                   elm.click();""".format(css=self.css, index=self.index)
        driver.execute_script(js)

    def remove_attribute(self, attribute):
        """
        删除某个元素的属性，比如日期空间的readonly属性
        """
        js = """
        var elm = document.querySelectorAll("{css}")[{index}];
            elm.removeAttribute("{attr}");
        """.format(css=self.css, index=self.index, attr=attribute)
        driver.execute_script(js)

    @staticmethod
    def remove_attr(element, attribute):
        js = """
        arguments[0].removeAttribute("{attr}");
        """.format(attr=attribute)
        driver.execute_script(js, element)

    @staticmethod
    def scrollTo(x, y):
        js = """
        window.scrollTo("{}", "{}")
        """.format(x, y)
        driver.execute_script(js)

    @staticmethod
    def window_scroll(element, x, y):
        js = """
        arguments[0].scrollTo("{}", "{}")
        """.format(x, y)
        driver.execute_script(js, element)

    def height_light(self):
        js = """
        var element = document.querySelectorAll("{css}")[{index}];
            element.style.border="2px solid red";
        """.format(css=self.css, index=self.index)
        driver.execute_script(js)

    @staticmethod
    def height_lig(element):
        js = """
        arguments[0].style.border="2px solid red";
        """
        driver.execute_script(js, element)


if __name__ == '__main__':
    pass
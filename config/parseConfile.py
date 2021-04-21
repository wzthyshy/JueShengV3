"""
-----------------------
-----------------------
注：封装获取配置文件里参数值
"""
import configparser

from JueShengV3.config.conf import CONF_PATH


class ParseConFile(object):
    def __init__(self):
        self.file = CONF_PATH
        self.conf = configparser.ConfigParser()
        # 读取配置文件
        self.conf.read(self.file, encoding='utf-8')

    def get_all_sections(self):
        """获取指定section下所有的option, 返回列表"""
        return self.conf.sections()

    def get_all_options(self, section):
        """获取指定section下所有的option, 返回列表"""
        return self.conf.options(section)

    def get_locator_or_options(self, section, option):
        """获取指定section, 指定option对应的数据, 返回元祖和字符串"""
        try:
            locator = self.conf.get(section, option)
            if '->' in locator:
                locator=tuple(locator.split('->'))
            return locator
        except configparser.NoOptionError as e:
            print('error', e)


if __name__ == '__main__':
    pass

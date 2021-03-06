import os
# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 报告目录 (join将项目根目录与文件名合成新的路径)
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
# ui对象库config.ini文件所在目录
CONF_PATH = os.path.join(ROOT_DIR, 'config', 'config.ini')

# 测试数据所在目录
DATA_Path = os.path.join(ROOT_DIR, 'data', '')
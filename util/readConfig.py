
import os

from config.configs import APP_ENV


def ReadConfig():
    # 读取配置环境参数
    path = os.path.dirname(os.path.dirname(__file__))
    if APP_ENV == 'test':
        path += '/config/test_env/'
    else:
        path += '/config/online_env/'
    path += 'group.ini'
    return path

def ReadConfig_1():
    # 读取配置环境参数
    path = os.path.dirname(os.path.dirname(__file__))
    if APP_ENV == 'test':
        path += '/config/test_env/'
    else:
        path += '/config/online_env/'
    path += 'group.ini'
    return path

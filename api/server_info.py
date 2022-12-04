# @Time    : 22/10/28 11:59
# @Author  : fyq
# @File    : server_info.py
# @Software: PyCharm

__author__ = 'fyq'


class ServerInfo:

    def __init__(self):

        # 主机标识 eg: http://192.168.1.1:8080
        self.host = None

        # 主机名
        self.host_name = None

        # 前缀
        self.prefix = None

        # cookie
        self.cookies = None

        # cookie的key
        self.cookies_name = None

        # token
        self.token = None

        # token的key
        self.token_name = None

        # token或者cookies获取时间戳
        self.ts = None

        # 过期时间
        self.expire_ts = None

        # master标识
        self.master_flag = None

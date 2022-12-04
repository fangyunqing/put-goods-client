# @Time    : 22/11/02 16:34
# @Author  : fyq
# @File    : master_server.py
# @Software: PyCharm

__author__ = 'fyq'

import tip
from api.handler.master import *
from .server_info import ServerInfo
import json
from constant import HttpMethod


class MasterServer:

    _SUCCESS = 200

    def __init__(self):
        self.server_info = ServerInfo()
        self.server_info.host = "http://10.104.3.18:8080"
        self.server_info.master_flag = True
        self.server_info.token_name = "token"
        self._login_url = self.server_info.host + "/login"

    def captcha_image(self, data_handler):
        CaptchaImageApi().send(server_info=self.server_info,
                               data=None,
                               data_handler=data_handler,
                               data_filter=self.data_filter)

    def login(self, data, data_handler):
        LoginApi().send(server_info=self.server_info,
                        data=data,
                        data_handler=data_handler,
                        data_filter=self.data_filter)

    def data_filter(self, data, reply):
        j = json.loads(data)
        if j["code"] != self._SUCCESS and "msg" in j.keys():
            tip.ERROR(None, j["msg"])
        # 如果是登录窗口 获取token
        url = reply.url().url()
        if self._login_url == url:
            if self.server_info.token_name in j:
                self.server_info.token = j[self.server_info.token_name]
            else:
                tip.ERROR(None, "令牌[{}]无法找到,请确认是否更换名称了".format(self.server_info.token_name))
        return j

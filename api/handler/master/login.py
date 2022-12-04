# @Time    : 22/11/04 14:11
# @Author  : fyq
# @File    : login.py
# @Software: PyCharm

__author__ = 'fyq'

from api.handler.abstract_api_handler import AbstractApiHandler
from util import convert_dict_2_bytearray
from constant import HttpMethod


class LoginApi(AbstractApiHandler):

    def add_token(self):
        return False

    def add_cookies(self):
        return False

    def http_method(self):
        return HttpMethod.POST

    def api(self):
        return "/login"

    def before_send(self, data):
        """
        :param data: list [username, password, code(验证码), uuid]
        :return:
        """
        assert len(data) > 3

        data_dict = {
            "username": data[0],
            "password": data[1],
            "code": data[2],
            "uuid": data[3]
        }

        return convert_dict_2_bytearray(data_dict)

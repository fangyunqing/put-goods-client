# @Time    : 22/11/02 14:01
# @Author  : fyq
# @File    : api_handler.py
# @Software: PyCharm

__author__ = 'fyq'

from abc import ABCMeta, abstractmethod


class IApiHandler(metaclass=ABCMeta):
    """
        api处理器 抽象 发和收
    """

    @abstractmethod
    def send(self, server_info, data, data_filter, data_handler):
        pass

    @abstractmethod
    def recv(self, data, reply):
        pass

    @abstractmethod
    def before_send(self, data):
        pass

    @abstractmethod
    def content_type(self):
        pass

    @abstractmethod
    def add_token(self):
        pass

    @abstractmethod
    def add_cookies(self):
        pass

    @abstractmethod
    def http_method(self):
        pass



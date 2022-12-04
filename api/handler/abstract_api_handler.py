# @Time    : 22/11/02 14:37
# @Author  : fyq
# @File    : abstract_api_handler.py
# @Software: PyCharm

__author__ = 'fyq'

from abc import abstractmethod

from .api_handler import IApiHandler
from network import network_holder
from constant import HttpMethod
from constant import ContentType


class AbstractApiHandler(IApiHandler):

    def content_type(self):
        return ContentType.JSON

    def add_token(self):
        return True

    def add_cookies(self):
        return True

    def http_method(self):
        return HttpMethod.GET

    def send(self, server_info, data, data_filter, data_handler):

        data = self.before_send(data)

        if self.http_method() == HttpMethod.GET:
            network_holder.get(server_info=server_info,
                               api=self.api(),
                               data=data,
                               add_token=self.add_token(),
                               add_cookies=self.add_cookies(),
                               data_handler=self.recv,
                               content_type=self.content_type())
        elif self.http_method() == HttpMethod.POST:
            network_holder.post(server_info=server_info,
                                api=self.api(),
                                data=data,
                                add_token=self.add_token(),
                                add_cookies=self.add_cookies(),
                                data_handler=self.recv,
                                content_type=self.content_type())
        else:
            return

        self.exec_func = data_handler
        self.filter_func = data_filter

    def recv(self, data, reply):
        if self.filter_func:
            data = self.filter_func(data, reply)
            if data:
                self.exec_func(data)
        else:
            self.exec_func(data)

        self.exec_func = None
        self.filter_func = None

    def before_send(self, data):
        return data

    def __init__(self):
        super(AbstractApiHandler, self).__init__()
        self.exec_func = None
        self.filter_func = None

    @abstractmethod
    def api(self):
        pass

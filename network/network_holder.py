# @Time    : 22/10/28 11:21
# @Author  : fyq
# @File    : network_holder.py
# @Software: PyCharm

__author__ = 'fyq'

from urllib.parse import urljoin

from PyQt5.QtCore import QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
import tip
import constant
from .network_error_map import NetworkErrorMap


class NetworkHolder:

    def __init__(self):
        self._network = QNetworkAccessManager()
        self._network.finished.connect(self.handle_response)
        self._handle_data_dict = {}
        self._network_error_map = NetworkErrorMap()

    def handle_response(self, reply):
        url = reply.url().url()
        error = reply.error()
        if error != 0:
            tip.ERROR(self._network_error_map.error_message(error))
            return
        if url in self._handle_data_dict.keys():
            recv = self._handle_data_dict.pop(url)
            recv(reply.readAll().data().decode(), reply)

    @staticmethod
    def _create_request(server_info,
                        api,
                        add_cookies=True,
                        add_token=True,
                        content_type=constant.ContentType.HTML):
        # 生成url
        host_name = server_info.host_name if server_info.host_name else "未知系统"
        if server_info.host is None:
            raise Exception("{}未配置host".format(host_name))
        else:
            host = server_info.host.strip()
            if len(host) == 0:
                raise Exception("{}未配置host".format(host_name))

        if api is None:
            raise Exception("{}的接口是空".format(host_name))
        else:
            api = api.strip()
            if len(api) == 0:
                raise Exception("{}的接口是空".format(host_name))
            elif server_info.prefix and len(server_info.prefix) > 0:
                api = "/" + server_info.prefix + api

        url = urljoin(urljoin(host, server_info.prefix), api)
        # request
        req = QNetworkRequest(QUrl(url))
        # cookies
        if add_cookies and server_info.cookies and len(server_info.cookies) > 0:
            cookies_name = server_info.cookies_name if server_info.cookies_name and len(server_info.cookies_name) > 0 \
                else "COOKIES"
            req.setHeader(cookies_name, server_info.cookies)
        # token
        if add_token and server_info.token and len(server_info.token) > 0:
            token_name = server_info.token_name if server_info.token_name and len(server_info.token_name) > 0 \
                else "token"
            req.setHeader(token_name, server_info.token)
        # content_type
        if content_type and len(content_type) > 0:
            req.setHeader(QNetworkRequest.ContentTypeHeader, content_type)

        return req

    def post(self,
             server_info,
             api,
             data,
             data_handler,
             add_cookies=True,
             add_token=True,
             content_type=constant.ContentType.JSON):
        req = self._create_request(server_info, api, add_cookies, add_token, content_type)
        self._handle_data_dict[req.url().url()] = data_handler
        self._network.post(req, data)

    def get(self,
            server_info,
            api,
            data,
            data_handler,
            add_cookies=True,
            add_token=True,
            content_type=constant.ContentType.HTML):
        req = self._create_request(server_info=server_info,
                                   api=api,
                                   add_cookies=add_cookies,
                                   add_token=add_token,
                                   content_type=content_type)
        self._handle_data_dict[req.url().url()] = data_handler
        send_data = None
        if isinstance(data, dict):
            data_list = []
            for key in data.keys():
                data_list.append(key + "=" + data[key])
            send_data = "&".join(data_list)
        elif isinstance(data, list):
            send_data = "&".join(data)
        elif isinstance(data, str):
            send_data = data
        if send_data:
            req.setUrl(QUrl(req.url().url() + "?" + send_data))
        self._network.get(req)

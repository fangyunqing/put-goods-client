# @Time    : 22/11/03 11:25
# @Author  : fyq
# @File    : server_manager.py
# @Software: PyCharm

__author__ = 'fyq'

from .master_server import MasterServer


class ServerManager:

    def __init__(self):
        self._server_list = []
        self._server_list.append(MasterServer())

    def get_master_server(self):
        filter_server_list = list(filter(lambda server: server.server_info.master_flag, self._server_list))
        if len(filter_server_list) > 0:
            return filter_server_list[0]

    def get_server(self, host_name):
        pass

# @Time    : 22/12/03 10:33
# @Author  : fyq
# @File    : login_server_dialog.py
# @Software: PyCharm

__author__ = 'fyq'

from PyQt5.QtWidgets import QDialog, QHBoxLayout

from frame.component import CommonTitle
from frame.login_server.login_server_designer import Ui_Dialog
from network.brower import WebEngineLoginView


class LoginServerDialog(QDialog, Ui_Dialog):
    def __init__(self, server_info):
        super(LoginServerDialog, self).__init__()
        # 水平布局
        self.setLayout(QHBoxLayout(parent=self))
        self.common_title = CommonTitle(self, self, max_icon=False, min_icon=True)
        # 服务器登录窗口
        self.layout().addWidget(WebEngineLoginView(server_info=server_info, parent=self))



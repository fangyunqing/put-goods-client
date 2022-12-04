# @Time    : 22/10/27 15:33
# @Author  : fyq
# @File    : login_dialog.py
# @Software: PyCharm

__author__ = 'fyq'

import base64

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog

from frame.component import CommonTitle
from frame.login.login_designer import Ui_Dialog
from api import g_server_manager
import tip


class LoginDialog(QDialog, Ui_Dialog):

    def __init__(self):
        super(LoginDialog, self).__init__()
        self.setupUi(self)
        self.master_server = g_server_manager.get_master_server()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.captcha_image_uuid = None
        self.login_button.clicked.connect(self.handle_login_click)
        self.captcha_image_label.mouseReleaseEvent = \
            lambda mr: self.master_server.captcha_image(data_handler=self.handle_captcha_image_click_callback)

        self.common_title = CommonTitle(self, self, max_icon=False, min_icon=True)

    def showEvent(self, QShowEvent):
        self.master_server.captcha_image(data_handler=self.handle_captcha_image_click_callback)

    def handle_login_click(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        captcha = self.captcha_edit.text()

        if not username or len(username) == 0:
            tip.WARNING(self, "请输入账户")
            return

        if not password or len(password) == 0:
            tip.WARNING(self, "请输入密码")
            return

        if not captcha or len(captcha) == 0:
            tip.WARNING(self, "请输入验证码")
            return

        self.master_server.login(data_handler=self.handle_login_click_callback,
                                 data=[username, password, captcha, self.captcha_image_uuid])

    def handle_captcha_image_click_callback(self, data):
        if "img" in data:
            image = base64.b64decode(data["img"])
            pix = QPixmap()
            pix.loadFromData(image)
            self.captcha_image_label.setScaledContents(True)
            self.captcha_image_label.setPixmap(pix)
            if "uuid" in data:
                self.captcha_image_uuid = data["uuid"]

    def handle_login_click_callback(self, data):
        if data["code"] != 200:
            self.master_server.captcha_image(data_handler=self.handle_captcha_image_click_callback)

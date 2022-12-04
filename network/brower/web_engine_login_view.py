# @Time    : 22/12/02 15:00
# @Author  : fyq
# @File    : web_engine_login_view.py
# @Software: PyCharm

__author__ = 'fyq'

from PyQt5.QtCore import QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile


class WebEngineLoginView(QWebEngineView):
    def __init__(self, server_info, *args, **kwargs):
        super(WebEngineLoginView, self).__init__(*args, **kwargs)
        # 服务器信息
        self.server_info = server_info
        # 绑定cookie被添加的信号槽
        QWebEngineProfile.defaultProfile().cookieStore().cookieAdded.connect(self.add_cookie)
        # 存放cookie字典
        self.cookies = {}
        # 定时器
        self.time = QTimer()
        self.time.timeout.connenct(self.check_login)
        self.time.start(1000)

    def add_cookie(self, cookie):
        # 将cookie保存到字典里
        name = cookie.name().data().decode('utf-8')
        value = cookie.value().data().decode('utf-8')
        self.cookies[name] = value

    def get_cookie(self):
        cookie_str = ''
        for key, value in self.cookies.items():  # 遍历字典
            cookie_str += (key + '=' + value + ';')  # 将键值对拿出来拼接一下
        return cookie_str

    def check_login(self):
        if self.server_info.check_cookie(self.cookies):
            pass


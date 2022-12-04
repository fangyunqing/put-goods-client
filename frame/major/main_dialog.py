# @Time    : 22/12/02 11:52
# @Author  : fyq
# @File    : main_dialog.py
# @Software: PyCharm

__author__ = 'fyq'

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QDialog

from frame.component import CommonTitle
from frame.major.major_designer import Ui_Dialog
from network.brower import WebEngineView


class MajorDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(MajorDialog, self).__init__()
        self.a = WebEngineView()
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.common_title = CommonTitle(self, self.frame_right, max_icon=True, min_icon=True)
        self.pushButton.clicked.connect(self.aaa)
        self.pushButton_2.clicked.connect(self.bbb)

    def aaa(self, event):
        self.a.show()
        self.a.setUrl(QUrl("https://www.nyedu.cn/"))
        self.frame_right.layout().addWidget(self.a)

    def bbb(self, event):
        print(self.a.get_cookie())

# @Time    : 22/11/07 13:12
# @Author  : fyq
# @File    : common_title.py
# @Software: PyCharm

__author__ = 'fyq'

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QApplication, QStyle
from PyQt5.QtGui import QIcon, QPixmap


class CommonTitle(QFrame):
    """
        通过标题栏
    """

    def __init__(self, parent, main_frame: QFrame, max_icon=False, min_icon=False):
        super(CommonTitle, self).__init__(parent=parent)
        self.main_parent = parent
        self.main_frame = main_frame
        self.main_parent .setAttribute(Qt.WA_TranslucentBackground)
        self.main_parent .setWindowFlags(Qt.FramelessWindowHint)

        qq = QFrame(parent)
        qq.setMinimumSize(QtCore.QSize(0, 0))
        qq.setMaximumSize(QtCore.QSize(16777215, 16777215))
        qq.setStyleSheet("QPushButton { border: none; }"
                         "QPushButton:hover { background-color:rgba(191, 191, 191, 50); }"
                         "QPushButton:pressed { background-color: rgba(100,100,100,1); }")
        qq.setFrameShape(QtWidgets.QFrame.StyledPanel)
        qq.setFrameShadow(QtWidgets.QFrame.Raised)
        qq.setObjectName("qq")
        qq.setLayout(main_frame.layout())

        self.verticalLayout = QtWidgets.QVBoxLayout(parent)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("11111111111")

        self.verticalLayout.addWidget(self)

        self.verticalLayout.addWidget(qq)
        main_frame.setLayout(self.verticalLayout)

        self.setMinimumSize(QtCore.QSize(0, 20))
        self.setMaximumSize(QtCore.QSize(16777215, 20))
        self.setStyleSheet("QPushButton { border: none; }"
                           "QPushButton:hover { background-color:rgba(191, 191, 191, 50); }"
                           "QPushButton:pressed { background-color: rgba(100,100,100,1); }")
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("title_frame")
        # 水平布局
        horizontal_layout = QtWidgets.QHBoxLayout(self)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        horizontal_layout.setObjectName("horizontal_layout")
        # 水平弹簧
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacer_item)
        # 最小化按钮
        if min_icon:
            min_push_button = QtWidgets.QPushButton(self)
            min_push_button.setIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMinButton))
            min_push_button.setObjectName("min_push_button")
            min_push_button.clicked.connect(self.main_parent.showMinimized)
            min_push_button.setToolTip("最小化")
            horizontal_layout.addWidget(min_push_button)
        # 还原按钮
        if max_icon:
            self.max_icon_button = QtWidgets.QPushButton(self)
            self.max_icon_button.setObjectName("max_icon_button")
            self.max_icon_button.clicked.connect(self.handle_max)
            horizontal_layout.addWidget(self.max_icon_button)
            self.handle_max()
        # 关闭按钮
        close_push_button = QtWidgets.QPushButton(self)
        close_push_button.setIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton))
        close_push_button.setObjectName("close_push_button")
        close_push_button.setToolTip("关闭")
        close_push_button.clicked.connect(self.main_parent.close)
        horizontal_layout.addWidget(close_push_button)
        # 窗口移动
        self.start_x = None
        self.start_y = None
        self.old_mouse_press_event = self.main_parent.mousePressEvent
        self.old_mouse_release_event = self.main_parent.mouseReleaseEvent
        self.old_mouse_move_event = self.main_parent.mouseMoveEvent
        self.main_parent.mousePressEvent = self.new_mouse_press_event
        self.main_parent.mouseReleaseEvent = self.new_mouse_release_event
        self.main_parent.mouseMoveEvent = self.new_mouse_move_event

    def new_mouse_press_event(self, event):
        if callable(self.old_mouse_press_event):
            self.old_mouse_press_event(event)
        if event.button() == Qt.LeftButton:
            self.start_x = event.x()
            self.start_y = event.y()

    def new_mouse_release_event(self, event):
        if callable(self.old_mouse_release_event):
            self.old_mouse_release_event(event)
        self.start_x = None
        self.start_y = None

    def new_mouse_move_event(self, event):
        if callable(self.old_mouse_move_event):
            self.old_mouse_move_event(event)
        if self.start_y and self.start_x:
            dis_x = event.x() - self.start_x
            dis_y = event.y() - self.start_y
            self.main_parent.move(self.main_parent.x() + dis_x, self.main_parent.y() + dis_y)

    def handle_max(self):
        if self.parent().isMaximized():
            self.parent().showNormal()
            self.max_icon_button.setIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMaxButton))
            self.max_icon_button.setToolTip("最大化")
        else:
            self.parent().showMaximized()
            self.max_icon_button.setIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarNormalButton))
            self.max_icon_button.setToolTip("还原")

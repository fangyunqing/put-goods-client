# @Time    : 22/11/04 9:46
# @Author  : fyq
# @File    : tip_manager.py
# @Software: PyCharm

__author__ = 'fyq'

from PyQt5.QtWidgets import QMessageBox


class TipManager:

    @staticmethod
    def info(parent, text, title="提示"):
        QMessageBox.information(parent,
                                title,
                                text,
                                QMessageBox.Yes,
                                QMessageBox.Yes)

    @staticmethod
    def question(parent, text, title="问题"):
        QMessageBox.question(parent,
                             title,
                             text,
                             QMessageBox.Yes,
                             QMessageBox.Yes)

    @staticmethod
    def warning(parent, text, title="警告"):
        QMessageBox.warning(parent,
                            title,
                            text,
                            QMessageBox.Yes,
                            QMessageBox.Yes)

    @staticmethod
    def error(parent, text, title="错误"):
        QMessageBox.critical(parent,
                             title,
                             text,
                             QMessageBox.Yes,
                             QMessageBox.Yes)

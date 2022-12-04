# @Time    : 22/11/04 11:08
# @Author  : fyq
# @File    : convert.py
# @Software: PyCharm

__author__ = 'fyq'

import json

from PyQt5.QtCore import QByteArray


def convert_dict_2_bytearray(data: dict):
    j = json.dumps(data)
    return QByteArray(j.encode())

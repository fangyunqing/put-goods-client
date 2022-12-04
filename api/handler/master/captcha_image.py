# @Time    : 22/11/02 14:39
# @Author  : fyq
# @File    : captcha_image.py
# @Software: PyCharm

__author__ = 'fyq'

from api.handler.abstract_api_handler import AbstractApiHandler
from constant import ContentType


class CaptchaImageApi(AbstractApiHandler):

    def content_type(self):
        return ContentType.HTML

    def add_token(self):
        return False

    def add_cookies(self):
        return False

    def api(self):
        return "/captchaImage"


"""

=====================

"""

import logging
import os

from flask import current_app as app
from werkzeug.exceptions import InternalServerError

from app.messages.errors import ERROR_APP_DEFAULT
from app.orm import STATUS_KEY, MESSAGE_KEY, MESSAGE_CODE_KEY

__author__ = "vishalkumar9565@gmail.com"

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)


class AppError(InternalServerError):
    """
    Application error which can be used anywhere in the application
    """

    def __init__(self, msg_code, msg, status=500):
        self.status = status
        self.msg_code = msg_code
        self.msg = msg
        super().__init__(description=self.msg)

    @staticmethod
    def get_default_instance():
        app.logger.info(ERROR_APP_DEFAULT[0], exc=True)
        AppError(*ERROR_APP_DEFAULT)

    def to_dict(self):
        return {STATUS_KEY: self.status,
                MESSAGE_CODE_KEY: self.msg_code,
                MESSAGE_KEY: self.msg}

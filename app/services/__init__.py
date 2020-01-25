"""

=====================

"""

import logging
import os

from utils.logging_helper import load_logger

__author__ = "vishalkumar9565@gmail.com"

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':
    load_logger(_LOGGER_PATH)

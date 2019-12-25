"""

=====================

"""

import logging
import os

from utils.logging_helper import load_logger
from flask_sqlalchemy import SQLAlchemy
__author__ = "vishalkumar9565@gmail.com"

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)

db = SQLAlchemy()

DATABASE_BIND_KEY = "speed_db"
DATABASE_NAME = "speed"
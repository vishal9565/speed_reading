"""

=====================

"""

import logging
import os
from contextlib import contextmanager

from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy

__author__ = "vishalkumar9565@gmail.com"

from flask_user import UserManager

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)

db = SQLAlchemy()

DATABASE_BIND_KEY = "speed_db"
DATABASE_NAME = "speed"

STATUS_KEY = "status"
MESSAGE_CODE_KEY = "msg_code"
MESSAGE_KEY = "message"


@contextmanager
def transactional_session():
    session = db.session
    try:

        # Yield the session
        yield session
        session.commit()

    except Exception as ex:

        # Rollback on error
        session.rollback()

        # Log the exception
        app.logger.error("Rolling back session changes due to errors...")

        raise

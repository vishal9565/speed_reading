"""
App initialization
=====================
The module creates an app and initialises
"""

import logging
import os

from flask import Flask

__author__ = "vishalkumar9565@gmail.com"

from app.controllers.login import login_blueprint
from app.controllers.passage import passage
from app.orm import db, DATABASE_BIND_KEY, DATABASE_NAME
from app.orm.models.users import Users
from app.orm.models.passage import Passage
_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)


def create_app():
    """
    Flask app creation and initialisation

    :return: Flask app instance
    :rtype:`flask.app.Flask`
    """
    app_instance = Flask(__name__,
                         static_folder="web/static",
                         template_folder="web/pages")

    # attaching blueprint here with the app
    app_instance.register_blueprint(blueprint=login_blueprint)
    app_instance.register_blueprint(blueprint=passage)

    # TODO : register error handlers

    app_instance.config.from_pyfile("../config/default.py", silent=False)

    # sql-alchemy variable initialisation

    app_instance.config["SQLALCHEMY_BINDS"] = {
        DATABASE_BIND_KEY: os.environ["APP_DB"]
    }

    with app_instance.app_context():
        # attaching db to app
        db.init_app(app=app_instance)
        db.create_all(bind=DATABASE_BIND_KEY)

    return app_instance

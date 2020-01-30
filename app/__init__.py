"""
App initialization
=====================
The module creates an app and initialises
"""

import logging
import os

from flask import Flask

__author__ = "vishalkumar9565@gmail.com"

from flask_user import UserManager


from app.controllers.passage import passage_blueprint
from app.errors.handler import handle_500, handle_404, handle_405, handle_401, handle_400
from app.orm import db, DATABASE_BIND_KEY, DATABASE_NAME
from app.orm.models.login import User
from app.orm.models.passage import Passage
from utils.converters import str2bool

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
    # app_instance.register_blueprint(blueprint=login_blueprint)
    app_instance.register_blueprint(blueprint=passage_blueprint)

    # TODO : register error handlers
    # Register the error handlers
    app_instance.register_error_handler(400, handle_400)
    app_instance.register_error_handler(500, handle_500)
    app_instance.register_error_handler(404, handle_404)
    app_instance.register_error_handler(405, handle_405)
    app_instance.register_error_handler(401, handle_401)
    app_instance.config.from_pyfile("../config/default.py", silent=False)

    app_instance.logger = True

    # sql-alchemy variable initialisation
    app_instance.config["SQLALCHEMY_BINDS"] = {
        DATABASE_BIND_KEY: os.environ["APP_DB"]
    }

    app_instance.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "echo": str2bool(os.environ["SQLALCHEMY_ECHO"]),
        # "pool_size": int(os.environ["SQLALCHEMY_POOL_SIZE"]),
        # "max_overflow": int(os.environ["SQLALCHEMY_MAX_OVERFLOW"]),
        # "pool_pre_ping": str2bool(os.environ["SQLALCHEMY_POOL_PRE_PING"]),
        # "pool_recycle": int(os.environ["SQLALCHEMY_POOL_RECYCLE"])

    }

    with app_instance.app_context():
        # attaching db to app
        db.init_app(app=app_instance)
        db.create_all(bind=DATABASE_BIND_KEY)
    user_manager = UserManager(app_instance, db=db, UserClass=User)

    return app_instance

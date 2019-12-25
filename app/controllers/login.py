"""
Login based routes
=====================
This module contains the blueprint related to login and sign up
"""

import logging
import os

from flask import Blueprint

__author__ = "vishalkumar9565@gmail.com"

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)

# creating the login blueprint

login_blueprint = Blueprint(name="login", import_name=__name__)


@login_blueprint.route("/login")
def login():
    LOGGER.warning("DO the login here")
    return "hurrey speedy, initial app is setup"

# -*- coding: UTF-8 -*-
"""
security configurations
========================
security details described for the app

"""
import logging
import os

__author__ = "vishal@gyandata.com"

LOGGER = logging.getLogger(__name__)


class Config(object):
    # use this key to secure CSRF attack in forms
    SECRET_KEY = os.environ.get("SECRET_KEY")
    print("inside config class and logger is not working!!")
    LOGGER.info(f"Database url is set as {os.environ.get('DATABASE_URL')}")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

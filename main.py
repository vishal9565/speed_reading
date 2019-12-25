"""
Main module
=====================
Main module for running the flask app
"""

import logging
import os

from app import create_app
from utils.logging_helper import load_logger

__author__ = "vishalkumar9565@gmail.com"

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)

app_instance = create_app()

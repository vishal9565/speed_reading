"""
Passage based routes
=====================
This contains passage related tables and its questions
"""

import logging
import os

from flask import Blueprint

__author__ = "vishalkumar9565@gmail.com"

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)

# creating the login blueprint

passage = Blueprint(name="passage", import_name=__name__)


@passage.route("/passage")
def get_passage():
    return "Passage is about to come"

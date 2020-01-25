"""

=====================

"""

import logging
import os

__author__ = "vishalkumar9565@gmail.com"

from flask import jsonify

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)


def str2bool(val):
    """
    string to bool conversion
    :param val: Bool value in string format ['True'/'False'/'0','1']
    :type val: str

    :return: boolean value
    :rtype: bool
    """
    if not issubclass(type(val), str):
        raise TypeError(f"Invalid argument passed requires str but got {type(val)}")
    if val.lower() == "true" or val.lower() == '1':
        return True
    return False


def my_jsonify(obj):
    """
    This returns json for the particular object
    :param obj: list or object
    :type obj: [list,object]

    :return: serialise json
    :rtype: str
    """

    if issubclass(type(obj), list):
        return jsonify([it._asdict() for it in obj])

    return jsonify(obj._asdict())


def create_dict(obj):
    """
    This returns json for the particular object
    :param obj: list or object
    :type obj: [list,object]

    :return: create dictionary
    :rtype: dict
    """

    if issubclass(type(obj), list):
        return [it._asdict() for it in obj]

    return obj._asdict()


def create_recursive_dict(obj):
    """
    This returns json for the particular object
    :param obj: list or object
    :type obj: [list,object]

    :return: create dictionary
    :rtype: dict
   """
    if issubclass(type(obj), list):
        pass
    pass

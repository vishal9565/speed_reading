"""
LOGGING HELPER FUNCTION
=========================
Module implements various Logger method like loading the logger configurations etc.

"""
import json
import logging.config
import os

__author__ = "vishalkumar9565@gmail.com"


def load_logger(config_json_path):
    """
    loads the json configuration to the logger

    :param config_json_path: path to logger json
    :type config_json_path: str

    :return:nothing
    :rtype: None
    """
    if not issubclass(type(config_json_path), str):
        raise TypeError(f"Invalid argument passed for config_json_path, requires str")

    if not os.path.isfile(config_json_path):
        raise ValueError(f"{config_json_path} is not a file")

    with open(config_json_path, 'r') as fp:
        logger_config_dict = json.load(fp)

    logging.config.dictConfig(config=logger_config_dict)

    return None

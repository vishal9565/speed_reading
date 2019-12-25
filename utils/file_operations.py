"""
I/O operations
==========================
Module implements the io function like checking the file whether that exists or not and various
other kind of file operation

"""
import json
import logging
import os

__author__ = "vishalkumar9565@gmail.com"

LOGGER = logging.getLogger(__name__)


def load_json(file_path):

    with open(file=file_path,mode='r') as fptr:
        json_dict = json.load(fp=fptr)
    return json_dict


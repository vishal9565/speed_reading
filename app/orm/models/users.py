"""
Users model
=====================
Users model to create user table
"""

import logging
import os

from sqlalchemy import Column, VARCHAR

from app.orm import db, DATABASE_BIND_KEY

__author__ = "vishalkumar9565@gmail.com"

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)


class Users(db.Model):
    """
    user information is stored in this table
    """

    __bind_key__ = DATABASE_BIND_KEY
    __tablename__ = "users"
    __table_args__ = {"mysql_engine": "InnoDB"}

    first_name = Column(VARCHAR(25), nullable=False, primary_key=True)
    last_name = Column(VARCHAR(25), nullable=False)
    gmail = Column(VARCHAR(250), nullable=False)
    password = Column(VARCHAR(250), nullable=False)

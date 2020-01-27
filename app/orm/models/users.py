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

from app.orm.models.common import BaseClass

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)


class Users(db.Model,BaseClass):
    """
    user information is stored in this table
    """

    __bind_key__ = DATABASE_BIND_KEY
    __tablename__ = "users"
    __table_args__ = {"mysql_engine": "InnoDB"}

    first_name = Column(VARCHAR(25), nullable=False, primary_key=True)
    last_name = Column(VARCHAR(25), nullable=False)
    gmail = Column(VARCHAR(250), nullable=False,unique=True)
    password = Column(VARCHAR(250), nullable=False)

    # define email getter
    @property
    def email(self):
        return self.gmail  # on user.email: return user.email_address

    # define email setter
    @email.setter
    def email(self, value):
        self.gmail = value
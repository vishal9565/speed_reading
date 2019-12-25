"""
Users model
=====================
Users model to create user table
"""

import logging
import os

from sqlalchemy import Column, VARCHAR, INTEGER, PrimaryKeyConstraint, ForeignKey

from app.orm import db, DATABASE_BIND_KEY

__author__ = "vishalkumar9565@gmail.com"

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)


class Passage(db.Model):
    """
    passage information
    """

    __bind_key__ = DATABASE_BIND_KEY
    __tablename__ = "passage"
    __table_args__ = {"mysql_engine": "InnoDB"}

    id = Column(INTEGER, nullable=False, autoincrement=True)
    paragraph_id = Column(INTEGER)
    paragraph = Column(VARCHAR(2000), nullable=False)

    PrimaryKeyConstraint(id, paragraph_id)


class Question(db.Model):
    """
        mcq questions corresponding to each passage
    """

    __bind_key__ = DATABASE_BIND_KEY
    __tablename__ = "question"
    __table_args__ = {"mysql_engine": "InnoDB"}

    passage_id = Column(INTEGER, ForeignKey(Passage.id))
    question_id = Column(INTEGER, autoincrement=True, primary_key=True)
    question = Column(VARCHAR(200), nullable=False)


class MultipleOptions(db.Model):
    """
        mcq questions options corresponding to each question
    """

    __bind_key__ = DATABASE_BIND_KEY
    __tablename__ = "multiple_option"
    __table_args__ = {"mysql_engine": "InnoDB"}

    question_id = Column(INTEGER, ForeignKey(Question.question_id))
    option_id = Column(INTEGER, autoincrement=True, primary_key=True)
    option_text = Column(VARCHAR(200), nullable=False)


class Answer(db.Model):
    """
        mcq answer options corresponding to each question
    """

    __bind_key__ = DATABASE_BIND_KEY
    __tablename__ = "answer"
    __table_args__ = {"mysql_engine": "InnoDB"}

    question_id = Column(INTEGER, ForeignKey(MultipleOptions.question_id))
    option_id = Column(INTEGER, ForeignKey(MultipleOptions.option_id))
    PrimaryKeyConstraint(question_id, option_id)

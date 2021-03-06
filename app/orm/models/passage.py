"""
Users model
=====================
Users model to create user table
"""

import logging
import os

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR
from sqlalchemy.orm import relationship

from app.orm import db, DATABASE_BIND_KEY
from app.orm.models.common import BaseClass

__author__ = "vishalkumar9565@gmail.com"

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)


class Passage(db.Model, BaseClass):
    """
    comprehension related information

    """
    __bind_key__ = DATABASE_BIND_KEY
    __tablename__ = "passage"
    __table_args__ = {"mysql_engine": "InnoDB"}

    id = Column(BIGINT,
                nullable=False,
                autoincrement=True,
                primary_key=True)
    name = Column(VARCHAR(255, unicode=True),
                  nullable=False,
                  unique=True)
    paragraphs = relationship("Paragraph",
                              lazy="select",
                              backref="passage",
                              cascade="save-update, merge, delete")
    questions = relationship("Question",
                             lazy="select",
                             backref="passage",
                             cascade="save-update, merge, delete")


class Paragraph(db.Model, BaseClass):
    """
    passage information
    """

    __bind_key__ = DATABASE_BIND_KEY
    __tablename__ = "paragraph"
    __table_args__ = {"mysql_engine": "InnoDB"}

    passage_id = Column(BIGINT,
                        ForeignKey(Passage.id,
                                   onupdate="CASCADE",
                                   ondelete="CASCADE"),
                        nullable=False)
    paragraph_id = Column(BIGINT,
                          primary_key=True,
                          autoincrement=True,
                          nullable=False)

    paragraph = Column(VARCHAR(4000, unicode=True), nullable=False)


class Question(db.Model, BaseClass):
    """
        mcq questions corresponding to each passage
    """

    __bind_key__ = DATABASE_BIND_KEY
    __tablename__ = "question"
    __table_args__ = {"mysql_engine": "InnoDB"}

    passage_id = Column(BIGINT,
                        ForeignKey(Passage.id,
                                   onupdate="CASCADE",
                                   ondelete="CASCADE"),
                        nullable=False)
    question_id = Column(BIGINT, autoincrement=True, primary_key=True)
    question = Column(VARCHAR(200, unicode=True), nullable=False)
    options = relationship("MultipleOption",
                           lazy="select",
                           backref="question",
                           cascade="save-update, merge, delete")
    correct_answer = relationship("Answer",
                                  lazy="select",
                                  backref="question",
                                  cascade="save-update, merge, delete")


class MultipleOption(db.Model, BaseClass):
    """
        mcq questions options corresponding to each question
    """

    __bind_key__ = DATABASE_BIND_KEY
    __tablename__ = "multiple_option"

    question_id = Column(BIGINT,
                         ForeignKey(Question.question_id,
                                    onupdate="CASCADE",
                                    ondelete="CASCADE"),
                         nullable=False)
    option_id = Column(BIGINT, autoincrement=True, primary_key=True)
    option_text = Column(VARCHAR(200, unicode=True), nullable=False)

    __table_args__ = ({"mysql_engine": "InnoDB"})


class Answer(db.Model, BaseClass):
    """
        mcq answer options corresponding to each question
    """

    __bind_key__ = DATABASE_BIND_KEY
    __tablename__ = "answer"

    id = Column(BIGINT, autoincrement=True, primary_key=True)
    question_id = Column(BIGINT,
                         ForeignKey(Question.question_id,
                                    onupdate="CASCADE",
                                    ondelete="CASCADE"))
    option_id = Column(BIGINT,
                       ForeignKey(MultipleOption.option_id,
                                  onupdate="CASCADE",
                                  ondelete="CASCADE"))

    __table_args__ = {"mysql_engine": "InnoDB"}

"""
Passage Queries
=====================
Passage related queries
"""
from sqlalchemy import func

from app.orm import db
from app.errors.exception import AppError
from app.messages.errors import *
from app.orm.models.passage import Passage, MultipleOption, Question

__author__ = "vishalkumar9565@gmail.com"


def get_passage(name):
    """
    Passage orm object
    :param name: name of the passage
    :type name: str
    :return: None or instance of passage orm
    :rtype: Union[None,app.orm.models.passage.Passage]

    """
    passage_obj = Passage.query.filter(Passage.name == name).one_or_none()
    return passage_obj


def get_passage_id(name):
    """
    Passage orm object
    :param name: name of the passage
    :type name: str
    :return: None or id of the object
    :rtype: Union[None,int]

    """
    passage_objs = Passage.query.filter(Passage.name == name).all()
    if len(passage_objs) > 1:
        raise AppError(*ERROR_MULTIPLE_OBJECT_FOUND)
    if len(passage_objs) == 0:
        raise AppError(*ERROR_NO_OBJECT_FOUND)
    return passage_objs[0].id


def get_question_id(**kwargs):
    """
    Passage orm object
    :param name: name of the passage
    :type name: str
    :return: None or id of the object
    :rtype: Union[None,int]

    """
    question_objs = Question.query.filter_by(**kwargs).all()
    if len(question_objs) > 1:
        raise AppError(*ERROR_MULTIPLE_OBJECT_FOUND)
    if len(question_objs) == 0:
        raise AppError(*ERROR_NO_OBJECT_FOUND)
    return question_objs[0].question_id


def get_option_id(**kwargs):
    """
    :param kwargs: dictionary containing question_id and as key and string as values

    :return:
    """
    passage_objs = MultipleOption.query.filter_by(**kwargs).all()
    # if len(passage_objs) > 1:
    #     raise AppError(*ERROR_MULTIPLE_OBJECT_FOUND)
    # if len(passage_objs) == 0:
    #     raise AppError(*ERROR_NO_OBJECT_FOUND)
    return passage_objs[0].option_id


def get_random_passage_id():
    """
    getting random id of the passage which is present in db
    :return: id of the passage
    :rtype :int
    """
    passage = Passage.query.order_by(func.rand()).first()
    if passage:
        return passage.id
    return passage

def get_fixed_passage_id():
    """
    getting fixed id of the passage which is present in db
    :return: id of the passage
    :rtype :int
    """
    passage = Passage.query.first()
    if passage:
        return passage.id
    return passage
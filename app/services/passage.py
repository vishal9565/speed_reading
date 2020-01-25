"""
Passage Service
=====================
Passage related services
"""

__author__ = "vishalkumar9565@gmail.com"

from app.errors.exception import AppError
from app.messages.errors import *
from app.messages.orm_errros import ERROR_DUPLICATE_PASSAGE_TITLE
from app.orm import transactional_session
from app.orm.models.passage import *


def create_passage(name):
    """

    :param name:
    :return:
    """
    exec_rec = Passage.query.filter(Passage.name == name).one_or_none()
    if exec_rec:
        raise AppError(*ERROR_DUPLICATE_PASSAGE_TITLE)
    passage = Passage()
    passage.name = name
    with transactional_session() as sess:
        sess.add(passage)


def create_paragraph(**kwargs):
    """
    create the Paragraph entity
    :param kwargs: dictionary containing the fields about the paragraph entity
    :type kwargs: dict

    :return: None if adding succeed else dictionary containing {"overwrite":true}
    :rtype Union[None,dict]
    """

    para = Paragraph()
    para.passage_id = kwargs["passage_id"]
    para.paragraph = kwargs["paragraph"]
    try:
        with transactional_session() as sess:
            sess.add(para)
    except:
        raise AppError(*ERROR_PARAGRAPH_CREATE)


def create_question(passage_id, question):
    """

    :param passage_id:
    :param question:
    :return:
    """
    question_obj = Question()
    question_obj.passage_id = passage_id
    question_obj.question = question

    try:
        with transactional_session() as sess:
            sess.add(question_obj)
    except:
        raise AppError(*ERROR_QUESTION_CREATE)


def create_multiple_option(question_id, option_text):
    """

    :param question_id:
    :param option_id:
    :param option_text:
    :return:
    """
    multi_obj = MultipleOption()
    multi_obj.question_id = question_id
    multi_obj.option_text = option_text
    try:
        with transactional_session() as sess:
            sess.add(multi_obj)
    except:
        raise AppError(*ERROR_MULTIPLE_OPTION_CREATE)


def create_answer(question_id, option_id):
    """

    :param question_id:
    :param option_id:
    :return:
    """
    answer_obj = Answer()
    answer_obj.question_id = question_id
    answer_obj.option_id = option_id
    try:
        with transactional_session() as sess:
            sess.add(answer_obj)
    except:
        raise AppError(*ERROR_MULTIPLE_OPTION_CREATE)

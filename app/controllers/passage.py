"""
Passage based routes
=====================
This contains passage related tables and its questions
"""

import logging
import os

from flask import Blueprint, request, render_template

from app.orm.models.passage import Passage

__author__ = "vishalkumar9565@gmail.com"

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)

# creating the login blueprint

passage = Blueprint(name="passage", import_name=__name__)


@passage.route("/passage/<int:id>")
def get_passage(id):
    if request.form:
        print(request.form)
        return request.form
    passage = Passage.query.filter(Passage.id == id).first()
    paragraphs = str.join("\n",[para.paragraph for para in passage.paragraphs])
    questions = passage.questions
    options = [question.options for question in questions]
    answers = [question.correct_answer for question in questions]
    # return my_jsonify(passage.questions[0].correct_answer[0].question.passage)
    # num_paras = len(passage.paragraphs)

    return render_template("passage.html",
                           passage=passage,
                           paragraphs=paragraphs,
                           questions=zip(questions, options, answers))


@passage.route("/add-passage")
def add_passage():

    return render_template("add_passage.html")
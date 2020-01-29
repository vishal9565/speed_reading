"""
Login based routes
=====================
This module contains the blueprint related to login and sign up
"""

import logging
import os

from flask import Blueprint, render_template_string, jsonify, render_template, request

from app.orm.models.passage import Passage
from app.orm import transactional_session
from app.orm.models.login import User

__author__ = "vishalkumar9565@gmail.com"

from app.orm.queries.passage import get_fixed_passage_id

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)

# creating the login blueprint

login_blueprint = Blueprint(name="login", import_name=__name__)

@login_blueprint.route("/", methods=["GET", "POST"])
def get_login_passage():
    id = get_fixed_passage_id()
    if id is None:
        return render_template("add_passage.html", output="No passage found. Please add a passage")
    if request.method == "POST":
        print(request.form)
        return request.form
    passage = Passage.query.filter(Passage.id == id).first()
    paragraphs = str.join("\n", [para.paragraph for para in passage.paragraphs])
    questions = passage.questions
    options = [question.options for question in questions]
    answers = [question.correct_answer for question in questions]
    # return my_jsonify(passage.questions[0].correct_answer[0].question.passage)
    # num_paras = len(passage.paragraphs)

    return render_template("login.html",
                           passage=passage,
                           paragraphs=paragraphs,
                           questions=zip(questions, options, answers))

# # The Home page is accessible to anyone
# @login_blueprint.route('/')
# def home_page():
#     return render_template_string("""
#         {% extends "flask_user_layout.html" %}
#         {% block content %}
#             <h2>Home page</h2>
#             <p><a href={{ url_for('user.register') }}>Register</a></p>
#
#             <p><a href={{ url_for('user.login') }}>Sign in</a></p>
#             <p><a href={{ url_for('login.home_page') }}>Home page</a> (accessible to anyone)</p>
#
#             <p><a href={{ url_for('user.logout') }}>Sign out</a></p>
#         {% endblock %}
#         """)

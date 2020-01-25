"""
Passage based routes
=====================
This contains passage related tables and its questions
"""

from flask import Blueprint, request, render_template

__author__ = "vishalkumar9565@gmail.com"

from app.orm.queries.passage import *
from app.services.passage import *
import pprint as pp

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)

# creating the login blueprint

passage_blueprint = Blueprint(name="passage", import_name=__name__)


@passage_blueprint.route("/passage")
def get_passage():
    id = get_random_passage_id()
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

    return render_template("passage.html",
                           passage=passage,
                           paragraphs=paragraphs,
                           questions=zip(questions, options, answers))


@passage_blueprint.route("/add-passage", methods=["GET", "POST"])
def add_passage():
    response_dict = request.form
    if request.method == "POST" and response_dict["title"] != "":
        pp.pprint(response_dict)

        create_passage(response_dict["title"])
        passage_id = get_passage_id(response_dict["title"])

        create_paragraph(passage_id=passage_id, paragraph=response_dict["paragraph"])

        # adding question 1
        question_no_str = "question-{}"
        for i in range(1, 5):
            question_no = question_no_str.format(i)
            if response_dict[question_no] != "":
                create_question(passage_id, response_dict[question_no])

                question_id = get_question_id(passage_id=passage_id,
                                              question=response_dict[question_no])
                option_no_str = "option-{i}{o}"
                option_dict = {}
                for option_num_iter in range(1, 5):
                    option_str = option_no_str.format(i=i, o=option_num_iter)
                    if response_dict[option_str] != "":
                        create_multiple_option(question_id=question_id,
                                               option_text=response_dict[option_str])
                        option_id = get_option_id(question_id=question_id,
                                                  option_text=response_dict[option_str])
                        option_dict[str(option_num_iter)] = option_id
                create_answer(question_id=question_id,
                              option_id=option_dict[response_dict["correct-{}".format(i)]])
        return render_template("add_passage.html", output="Passage added successfully")

    return render_template("add_passage.html")


@passage_blueprint.route("/test", methods=["GET"])
def test():
    return "success"

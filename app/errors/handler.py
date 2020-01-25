"""

=====================

"""

from flask import jsonify

from app.errors.exception import AppError

__author__ = "vishalkumar9565@gmail.com"

from app.messages.errors import ERROR_REQUEST_MALFORMED

from app.orm import STATUS_KEY, MESSAGE_CODE_KEY, MESSAGE_KEY


def handle_500(error):
    """
    Handle internal server error i.e. HTTP 500 code

    :param error: The internal server error
    :type error: a subclass of :class:`Exception`

    :return: A tuple of the json error message and the error code
    :rtype: tuple
    """
    # Our custom exception
    if issubclass(type(error), AppError):
        # Our application error. So get the error as a dictionary and convert it to json and
        # return it as a response
        return jsonify(error.to_dict()), error.status

    else:
        # Not our application error. So redirect to our 500 error page instead
        return jsonify("5 error, Please write this page")


def handle_404(error):
    """
    Handle page-not-found error i.e. HTTP 404 code

    :param error: The page-not-found error
    :type error: :class:`werkzeug.exceptions.NotFound`

    :return: A view
    """
    return jsonify("404 error, Please write this page")


def handle_405(error):
    """
    Handle method not allowed error i.e. HTTP 405 code

    :param error: The method not allowed error
    :type error: :class:`werkzeug.exceptions.MethodNotAllowed`

    :return: A tuple of the json error message and the error code
    :rtype: tuple
    """
    # Construct the dictionary
    err_dict = dict()

    # Add in the error code
    err_dict["code"] = error.code

    # Add in the error description
    err_dict["message"] = error.description

    # Construct the json and return
    return jsonify(err_dict), 405


def handle_401(error):
    """
    Handle unauthorized access error i.e. HTTP 401 code

    :param error: The unauthorized access error
    :type error: :class:`werkzeug.exceptions.Unauthorized`


    :return: A view
    """
    return jsonify("401 error. Please write this page")


def handle_403(error):
    """
    Handle forbidden access error i.e. HTTP 401 code

    :param error: The forbidden access error
    :type error: :class:`werkzeug.exceptions.Forbidden`


    :return: A view
    """

    return jsonify("403 error. Please write this page")


def handle_400(error):
    """
    Handle a bad request error. i.e. HTTP 400 code

    :param error: The bad request key error
    :type error: :class:`werkzeug.exceptions.BadRequestKeyError`

    :return: A tuple of the json error message and the error code
    :rtype: tuple
    """

    # Construct the dictionary
    err_dict = dict()

    err_dict[STATUS_KEY] = 400
    err_dict[MESSAGE_CODE_KEY] = ERROR_REQUEST_MALFORMED[1]
    err_dict[MESSAGE_KEY] = ERROR_REQUEST_MALFORMED[0]

    # Construct the json and return
    return jsonify(err_dict), 400

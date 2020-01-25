"""
Application related errors
===========================
Application related error string
"""

ERROR_APP_DEFAULT = ("Internal server error", "app.default.error")
ERROR_REQUEST_MALFORMED = ("Request is malformed ","error.app.orm.request_malformed")
ERROR_PARAGRAPH_CREATE = ("Error occurred during paragraph creation", "error.app.orm.create.paragraph.error")
ERROR_QUESTION_CREATE = ("Error occurred during question creation", "error.app.orm.create.question.error")
ERROR_MULTIPLE_OPTION_CREATE = ("Error occurred during multiple option instance creation", "error.app.orm.create.multi_option.error")


# queries error
ERROR_MULTIPLE_OBJECT_FOUND = ("multiple object found expect only one or for getting id","error.app.query.muliple_record.id")
ERROR_NO_OBJECT_FOUND = ("multiple object found expect only one or for getting id","error.app.query.muliple_record.id")
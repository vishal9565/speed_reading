"""
Login related ORMS
=====================
Login related ORMS
"""

from flask_user import UserMixin

from app.orm import db, DATABASE_BIND_KEY

__author__ = "vishalkumar9565@gmail.com"


# Define the User data-model.
# NB: Make sure to add flask_user UserMixin !!!
class User(db.Model, UserMixin):

    __bind_key__ = DATABASE_BIND_KEY
    __tablename__ = 'users'
    __table_args__ = {"mysql_engine": "InnoDB"}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')

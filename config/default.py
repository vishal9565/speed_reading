# The secret key used by flask
import os

SECRET_KEY = "d0bb74a24b4e7d5b14fd04eab84af1b5736b93931ea"
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///app.db"
SQLALCHEMY_TRACK_MODIFICATIONS = True
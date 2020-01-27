# The secret key used by flask
import os

SECRET_KEY = "d0bb74a24b4e7d5b14fd04eab84af1b5736b93931ea"
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///app.db"
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask-Mail SMTP server settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'email@example.com'
MAIL_PASSWORD = 'password'
MAIL_DEFAULT_SENDER = '"Speed Reading" <noreply@example.com>'

# Flask-User settings
USER_APP_NAME = "Speed Reading"  # Shown in and email templates and page footers
USER_ENABLE_EMAIL = True  # Enable email authentication
USER_ENABLE_USERNAME = False  # enable username authentication
USER_EMAIL_SENDER_NAME = USER_APP_NAME
USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
USER_ENABLE_CHANGE_PASSWORD = True
USER_ENABLE_CONFIRM_EMAIL=True
USER_ENABLE_FORGOT_PASSWORD=True
USER_ENABLE_REGISTER =True
USER_ENABLE_REMEMBER_ME = True
USER_AUTO_LOGIN = True
USER_AUTO_LOGIN_AFTER_CONFIRM = True
USER_AUTO_LOGIN_AFTER_REGISTER = True
USER_AUTO_LOGIN_AT_LOGIN = True


USER_AFTER_CHANGE_PASSWORD_ENDPOINT = ''
USER_AFTER_CHANGE_USERNAME_ENDPOINT = ''
USER_AFTER_CONFIRM_ENDPOINT = ''
USER_AFTER_EDIT_USER_PROFILE_ENDPOINT = ''
USER_AFTER_FORGOT_PASSWORD_ENDPOINT = ''
USER_AFTER_INVITE_ENDPOINT = ''
USER_AFTER_LOGIN_ENDPOINT = ''
USER_AFTER_LOGOUT_ENDPOINT = ''
USER_AFTER_REGISTER_ENDPOINT = ''
USER_AFTER_RESEND_EMAIL_CONFIRMATION_ENDPOINT = ''
USER_AFTER_RESET_PASSWORD_ENDPOINT = ''

USER_CHANGE_PASSWORD_TEMPLATE = 'web/pages/template/flask_user/change_password.html'
USER_CHANGE_USERNAME_TEMPLATE = 'web/pages/template/flask_user/change_username.html'
USER_CONFIRM_EMAIL_TEMPLATE = 'web/pages/template/flask_user/emails/confirm_email'
USER_EDIT_USER_PROFILE_TEMPLATE = 'web/pages/template/flask_user/edit_user_profile.html'
USER_FORGOT_PASSWORD_TEMPLATE = 'web/pages/template/flask_user/forgot_password.html'
USER_INVITE_USER_EMAIL_TEMPLATE = 'web/pages/template/flask_user/emails/invite_user'
USER_INVITE_USER_TEMPLATE = 'web/pages/template/flask_user/invite_user.html'
USER_LOGIN_AUTH0_TEMPLATE = 'web/pages/template/flask_user/login_auth0.html'
USER_LOGIN_TEMPLATE = 'web/pages/template/flask_user/login.html'
USER_MANAGE_EMAILS_TEMPLATE = 'web/pages/template/flask_user/manage_emails.html'
USER_PASSWORD_CHANGED_EMAIL_TEMPLATE = 'web/pages/template/flask_user/emails/password_changed'
USER_REGISTER_TEMPLATE = 'web/pages/template/flask_user/register.html'
USER_REGISTERED_EMAIL_TEMPLATE = 'web/pages/template/flask_user/emails/registered'
USER_RESEND_CONFIRM_EMAIL_TEMPLATE = 'web/pages/template/flask_user/resend_confirm_email.html'
USER_RESET_PASSWORD_EMAIL_TEMPLATE = 'web/pages/template/flask_user/emails/reset_password'
USER_RESET_PASSWORD_TEMPLATE = 'web/pages/template/flask_user/reset_password.html'
USER_USERNAME_CHANGED_EMAIL_TEMPLATE = 'web/pages/template/flask_user/emails/username_changed'

USER_CHANGE_PASSWORD_URL = '/user/change-password'
USER_CHANGE_USERNAME_URL = '/user/change-username'
USER_CONFIRM_EMAIL_URL = '/user/confirm-email/<token>'
USER_EDIT_USER_PROFILE_URL = '/user/edit_user_profile'
USER_EMAIL_ACTION_URL = '/user/email/<id>/<action>'
USER_FORGOT_PASSWORD_URL = '/user/forgot-password'
USER_INVITE_USER_URL = '/user/invite'
USER_LOGIN_URL = '/user/sign-in'
USER_LOGOUT_URL = '/user/sign-out'
USER_MANAGE_EMAILS_URL = '/user/manage-emails'
USER_REGISTER_URL = '/user/register'
USER_RESEND_EMAIL_CONFIRMATION_URL = '/user/resend-email-confirmation'
USER_RESET_PASSWORD_URL = '/user/reset-password/<token>'

USER_UNAUTHENTICATED_ENDPOINT = 'user.login'
USER_PASSWORD_HASH = 'sha512_crypt'
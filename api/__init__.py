import logging
from config import Config
from flask import Flask, request, g
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth
from flask_apispec.extension import FlaskApiSpec
from flask_babel import Babel

app = Flask(__name__, static_folder=Config.UPLOAD_FOLDER)
app.config.from_object(Config)

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
auth = HTTPBasicAuth()
docs = FlaskApiSpec(app)
babel = Babel(app)


@auth.verify_password
def verify_password(username_or_token, password):
    from api.models.user import UserModel
    # сначала проверяем authentication token
    print("username_or_token = ", username_or_token)
    print("password = ", password)
    user = UserModel.verify_auth_token(username_or_token)
    if not user:
        # потом авторизация
        user = UserModel.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


# @auth.get_user_roles
# def get_user_roles(data):
#     from api.models.user import UserModel
#     token = data['username']
#     user = UserModel.verify_auth_token(token)
#     return user.get_role()

# Accept-Language: da, en-gb;q=0.8, en;q=0.7
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

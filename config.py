import os
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

base_dir = os.path.dirname(os.path.abspath(__file__))
ma_plugin = MarshmallowPlugin()

security_definitions = {
    "basicAuth": {
        "type": "basic"
    }
}


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(base_dir, 'base.db')
    TEST_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    PORT = 5000
    SECRET_KEY = "qwerty"
    UPLOAD_FOLDER_NAME = 'upload'
    UPLOAD_FOLDER = os.path.join(base_dir, UPLOAD_FOLDER_NAME)
    APISPEC_SPEC = APISpec(
        title='Notes Project',
        version='v1',
        plugins=[ma_plugin],
        securityDefinitions=security_definitions,
        security=[],
        openapi_version='2.0.0'
    )
    APISPEC_SWAGGER_URL = '/swagger'
    APISPEC_SWAGGER_UI_URL = '/swagger-ui'
    RESTFUL_JSON = {
        'ensure_ascii': False
    }
    LANGUAGES = ['en', 'ru']

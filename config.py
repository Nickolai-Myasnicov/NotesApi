import os

base_dir = os.path.dirname(os.path.abspath(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(base_dir, 'base.db')
    TEST_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    PORT = 5000
    SECRET_KEY = "My secret key =)"
    UPLOAD_FOLDER_NAME = 'upload'
    UPLOAD_FOLDER = os.path.join(base_dir, UPLOAD_FOLDER_NAME)

# BAD
# GET: /notes/filter/tag/<tag_name>/author/<author_name>

# GOOD
# GET: /notes/filter?tag=<tag_name>&author=<author_name>

# EXCELENT
# GET: /notes?filter[tag]=<tag_name>

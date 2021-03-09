from api import api, app
from api.resources.user import UserResource
from api.resources.token import TokenResource
from config import Config

api.add_resource(UserResource,
                 '/users', '/users/<int:id>')
api.add_resource(TokenResource, '/auth/token')

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)

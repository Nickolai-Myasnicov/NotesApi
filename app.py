from api import api, app, docs
from api.resources.note import NoteResource
from api.resources.user import UserResource, UsersListResource
from api.resources.token import TokenResource
from config import Config


api.add_resource(UsersListResource,
                 '/users')                # GET

api.add_resource(UserResource,
                 '/users',                # POST
                 '/users/<int:user_id>')  # GET, PUT

api.add_resource(TokenResource, '/auth/token')

api.add_resource(NoteResource,
                 '/notes',                # GET, POST
                 '/notes/<int:note_id>',  # GET, PUT
                 )
docs.register(UserResource)

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)

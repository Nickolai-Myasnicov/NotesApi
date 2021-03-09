from api import api, app
from api.resources.note import NoteResource
from api.resources.user import UserResource
from api.resources.token import TokenResource
from config import Config

api.add_resource(UserResource,
                 '/users',                       # GET, POST
                 '/users/<int:user_id>')         # GET, PUT
api.add_resource(TokenResource, '/auth/token')
api.add_resource(NoteResource,
                 '/notes',                       # GET, POST
                 '/notes/<int:note_id>',         # GET, PUT
                 )

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)

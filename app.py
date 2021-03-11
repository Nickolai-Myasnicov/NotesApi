from api import api, app, docs
from api.resources.note import NoteResource, NotesListResource
from api.resources.user import UserResource, UsersListResource
from api.resources.token import TokenResource
from config import Config

api.add_resource(UsersListResource,
                 '/users')                       # GET, POST
api.add_resource(UserResource,
                 '/users/<int:user_id>')         # GET, PUT

api.add_resource(TokenResource, '/auth/token')

api.add_resource(NotesListResource,
                 '/notes',                       # GET, POST
                 )
api.add_resource(NoteResource,
                 '/notes/<int:note_id>',         # GET, PUT
                 )

docs.register(UserResource)
docs.register(UsersListResource)
docs.register(NoteResource)
docs.register(NotesListResource)
if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)

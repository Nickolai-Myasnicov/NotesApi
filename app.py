from api import api, app, docs
from api.resources.note import NoteResource, NotesListResource, NotesPublicResource
from api.resources.user import UserResource, UsersListResource
from api.resources.token import TokenResource
from config import Config


api.add_resource(UsersListResource,
                 '/users')                # GET
api.add_resource(UserResource,
                 '/users/<int:user_id>')  # GET, PUT

api.add_resource(TokenResource, '/auth/token')

api.add_resource(NotesListResource,
                 '/notes',
                 )
api.add_resource(NoteResource,
                 '/notes/<int:note_id>',
                 )
api.add_resource(NotesPublicResource,
                 '/notes/public',
                 )

docs.register(UserResource)
docs.register(UsersListResource)
docs.register(NoteResource)
docs.register(NotesListResource)
docs.register(NotesPublicResource)
if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)

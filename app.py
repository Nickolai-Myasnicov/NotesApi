from api import api, app, docs
from api.resources.note import NoteResource, NotesListResource, \
    NotesPublicResource, NoteSetTagsResource, NotesFilterResource

from api.resources.user import UserResource, UsersListResource
from api.resources.tag import TagResource, TagsListResource
from api.resources.token import TokenResource
from config import Config

# CRUD

# Create --> POST
# Read --> GET
# Update --> PUT
# Delete --> DELETE
api.add_resource(UsersListResource,
                 '/users')                       # GET, POST
api.add_resource(UserResource,
                 '/users/<int:user_id>')         # GET, PUT

api.add_resource(TagsListResource,
                 '/tags')                        # GET, POST
api.add_resource(TagResource,
                 '/tags/<int:tag_id>')           # GET, PUT

api.add_resource(TokenResource, '/auth/token')

api.add_resource(NotesListResource,
                 '/notes',                       # GET, POST
                 )
api.add_resource(NoteResource,
                 '/notes/<int:note_id>',         # GET, PUT
                 )
api.add_resource(NotesPublicResource,
                 '/notes/public',                # GET
                 )
api.add_resource(NoteSetTagsResource,
                 '/notes/<int:note_id>/tags',    # GET
                 )

# /notes/filter?tag=<tag_name>
api.add_resource(NotesFilterResource,
                 '/notes/filter',                # GET
                 )

docs.register(UserResource)
docs.register(UsersListResource)
docs.register(NoteResource)
docs.register(NotesListResource)
docs.register(NotesPublicResource)
docs.register(TagResource)
docs.register(TagsListResource)
docs.register(NoteSetTagsResource)
docs.register(NotesFilterResource)
if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)

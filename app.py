from api import api, app, docs
from api.resources.note import NoteResource, NotesListResource, \
    NotesPublicResource, NoteSetTagsResource, NotesFilterResource

from api.resources.user import UserResource, UsersListResource
from api.resources.tag import TagResource, TagsListResource
from api.resources.token import TokenResource
from api.resources.file import UploadPictureResource
from config import Config
from flask import render_template, send_from_directory


@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')


@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


# CRUD

# Create --> POST
# Read --> GET
# Update --> PUT
# Delete --> DELETE
api.add_resource(UsersListResource,
                 '/users')  # GET, POST
api.add_resource(UserResource,
                 '/users/<int:user_id>')  # GET, PUT

api.add_resource(TagsListResource,
                 '/tags')  # GET, POST
api.add_resource(TagResource,
                 '/tags/<int:tag_id>')  # GET, PUT

api.add_resource(TokenResource, '/auth/token')

api.add_resource(NotesListResource,
                 '/notes',  # GET, POST
                 )
api.add_resource(NoteResource,
                 '/notes/<int:note_id>',  # GET, PUT
                 )
api.add_resource(NotesPublicResource,
                 '/notes/public',  # GET
                 )
api.add_resource(NoteSetTagsResource,
                 '/notes/<int:note_id>/tags',  # GET
                 )

# /notes/filter?tag=<tag_name>
api.add_resource(NotesFilterResource,
                 '/notes/filter',  # GET
                 )

api.add_resource(UploadPictureResource,
                 "/upload",
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
docs.register(UploadPictureResource)
if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)

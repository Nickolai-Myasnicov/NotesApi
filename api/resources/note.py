from api import Resource, reqparse, db, auth, abort, g, api
from api.models.note import NoteModel
from api.schemas.note import NoteSchema, NoteRequestSchema
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs


@doc(tags=['Notes'])
class NoteResource(MethodResource):
    @marshal_with(NoteSchema)
    @auth.login_required
    def get(self, note_id):
        author = g.user
        note = NoteModel.query.get(note_id)
        if not note:
            abort(404, error=f"Note with id={note_id} not found")
        if note.author != author:
            abort(403, error=f"Forbidden")
        return note, 200

    @auth.login_required
    def put(self, note_id):
        note_parser = reqparse.RequestParser()
        note_parser.add_argument("text", required=True)
        note_data = note_parser.parse_args()
        author = g.user
        note = NoteModel.query.get(note_id)
        if not note:
            abort(404, error=f"note {note_id} not found")
        if note.author != author:
            abort(403, error=f"Forbidden")
        note.text = note_data["text"]
        note.save()
        return note, 200

    @auth.login_required
    def delete(self, quote_id):
        pass


@doc(tags=['Notes'])
class NotesListResource(MethodResource):
    @auth.login_required
    @marshal_with(NoteSchema(many=True))
    def get(self):
        author = g.user
        notes = NoteModel.query.filter_by(author_id=author.id)
        return notes, 200

    @auth.login_required
    @use_kwargs(NoteRequestSchema, location=('json'))
    @marshal_with(NoteSchema)
    def post(self, **kwargs):
        author = g.user
        print("author.username = ", author.username)
        note = NoteModel(author_id=author.id, **kwargs)
        note.save()
        return note, 201


class NotesPublicResource(MethodResource):
    @marshal_with(NoteSchema(many=True))
    def get(self):
        notes = NoteModel.query.filter_by(private=False)
        return notes, 200
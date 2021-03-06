from api import Resource, reqparse, db, auth, abort, g, api, app
from api.models.note import NoteModel
from api.models.tag import TagModel
from api.schemas.note import NoteSchema, NoteRequestSchema
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from webargs import fields
from flask_babel import _
import pdb


@doc(tags=['Notes'], security=[{"basicAuth": []}])
class NoteResource(MethodResource):
    @auth.login_required
    @marshal_with(NoteSchema)
    def get(self, note_id):
        author = g.user
        note = NoteModel.query.get(note_id)
        if not note:
            # app.logger.warning("Кто-то пытается получить нечто")
            # abort(404, error=f"Note with id={note_id} not found")
            abort(404, error=_("Note with id=%(note_id) not found"), note_id=note_id)
        if note.author != author:
            abort(403, error=_("Forbidden"))
        return note, 200

    @auth.login_required
    @use_kwargs(NoteRequestSchema, location=('json'))
    @marshal_with(NoteSchema)
    def put(self, note_id, **kwargs):
        author = g.user
        note = NoteModel.query.get(note_id)
        if not note:
            abort(404, error=f"note {note_id} not found")
        if note.author != author:
            abort(403, error=_(f"Forbidden"))
        note.text = kwargs["text"]
        note.private = kwargs["private"]
        note.save()
        return note, 200

    @auth.login_required
    @marshal_with(NoteSchema)
    def delete(self, note_id):
        note = NoteModel.query.get(note_id)
        note.delete()


@doc(tags=['Notes'], security=[{"basicAuth": []}])
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


@doc(tags=['Notes'])
class NotesPublicResource(MethodResource):
    @marshal_with(NoteSchema(many=True))
    def get(self):
        notes = NoteModel.query.filter_by(private=False)
        return notes, 200


@doc(tags=['Notes'])
class NoteSetTagsResource(MethodResource):
    @doc(summary="Set tags to Note")
    @use_kwargs({"tags": fields.List(fields.Int())}, location=('json'))
    @marshal_with(NoteSchema)
    def put(self, note_id, **kwargs):
        note = NoteModel.query.get(note_id)
        if not note:
            abort(404, error=f"note {note_id} not found")
        print("note kwargs = ", kwargs)
        for tag_id in kwargs["tags"]:
            tag = TagModel.query.get(tag_id)
            note.tags.append(tag)
        note.save()
        return note, 200


@doc(tags=['Notes'])
class NotesFilterResource(MethodResource):
    @use_kwargs({"tag": fields.Str()}, location=('query'))
    @marshal_with(NoteSchema(many=True))
    def get(self, **kwargs):
        # print("kwargs = ", kwargs)
        notes = NoteModel.query.filter(NoteModel.tags.any(name=kwargs['tag']))
        # pdb.set_trace()
        return notes, 200
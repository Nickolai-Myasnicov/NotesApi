from api import Resource, reqparse, db, auth, abort, g
from api.models.note import NoteModel
from api.schemas.note import note_schema, notes_schema


class NoteResource(Resource):
    def get(self, note_id=None):
        if note_id is None:
            notes = NoteModel.query.all()
            return notes_schema.dump(notes), 200

        note = NoteModel.query.get(note_id)
        if not note:
            abort(404, error=f"Note with id={note_id} not found")
        return note_schema.dump(note), 200

    @auth.login_required
    def post(self):
        note_parser = reqparse.RequestParser()
        note_parser.add_argument("text", required=True)
        note_data = note_parser.parse_args()
        author = g.user
        note = NoteModel(author_id=author.id, text=note_data["text"])
        db.session.add(note)
        db.session.commit()
        return note_schema.dump(note), 201

    @auth.login_required
    def put(self, quote_id):
        pass

    @auth.login_required
    def delete(self, quote_id):
        pass

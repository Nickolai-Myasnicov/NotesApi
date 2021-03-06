from api import ma
from api.models.note import NoteModel
from api.schemas.user import UserSchema
from api.schemas.tag import TagSchema


class NoteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = NoteModel

    id = ma.auto_field()
    text = ma.auto_field()
    private = ma.auto_field()
    author = ma.Nested(UserSchema())
    tags = ma.Nested(TagSchema(many=True))

    _links = ma.Hyperlinks({
        'self': ma.URLFor('noteresource', values=dict(note_id="<id>")),
        'collection': ma.URLFor('noteslistresource')
    })


class NoteRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = NoteModel

    text = ma.Str()
    private = ma.Bool(required=False)


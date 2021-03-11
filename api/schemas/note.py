from api import ma
from api.models.note import NoteModel
from api.schemas.user import UserSchema


class NoteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = NoteModel

    id = ma.auto_field()
    text = ma.auto_field()
    private = ma.auto_field()
    author = ma.Nested(UserSchema())


# Десериализация запроса(request)
class NoteRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = NoteModel

    text = ma.Str()
    private = ma.Bool(required=False)

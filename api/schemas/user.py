from api import ma
from api.models.user import UserModel


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel
        # fields = ('id', 'username')

    id = ma.auto_field()
    username = ma.auto_field()
    _links = ma.Hyperlinks({
        'self': ma.URLFor('userresource', values=dict(user_id="<id>")),
        'collection': ma.URLFor('UserListResource')
    })


class UserRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel

    username = ma.Str()
    password = ma.Str()


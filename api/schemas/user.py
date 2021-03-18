from api import ma
from api.models.user import UserModel


#       schema        flask-restful
# object ------>  dict ----------> json


# Сериализация ответа(response)
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        fields = ('id', 'username')

    id = ma.auto_field()
    username = ma.auto_field()
    _links = ma.Hyperlinks({
        'self': ma.URLFor('userresource', values=dict(user_id="<id>")),
        'collection': ma.URLFor('userslistresource')
    })


# Десериализация запроса(request)
class UserRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel

    username = ma.Str()
    password = ma.Str()

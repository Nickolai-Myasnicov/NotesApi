from api import ma
from api.models.user import UserModel


# Сериализация ответа(response)
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        fields = ('id', 'username')


# Десериализация запроса(request)
class UserRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel

    username = ma.Str()
    password = ma.Str()

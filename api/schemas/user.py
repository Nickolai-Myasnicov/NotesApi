from api import ma
from api.models.user import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        fields = ('id', 'username')


class UserRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel

    username = ma.Str()
    password = ma.Str()

# class UserRequestSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = UserModel
#
#     username = ma.Str()
#     password = ma.Str()

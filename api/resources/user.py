from api import Resource, abort
from api.models.user import UserModel
from api.schemas.user import UserSchema, UserRequestSchema
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs


@doc(tags=['Users'])
class UserResource(MethodResource):
    @marshal_with(UserSchema)
    @doc(
        summary="Get user by id",
        description="Returns user",
        produces=[
            'application/json'
        ],
        params={'user_id': {'description': 'user id'}},
        responses={
            "200": {

                "description": "Return user",
                "content":
                    {"application/json": []}

            },
            "404": {
                "description": "User not found"
            }
        }
    )
    # О прочих возможностях тут: https://swagger.io/specification/
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if not user:
            abort(404, error=f"User with id={user_id} not found")
        return user, 200


@doc(tags=['Users'])
class UsersListResource(MethodResource):
    @marshal_with(UserSchema(many=True))
    def get(self):
        users = UserModel.query.all()
        return users, 200

    @use_kwargs(UserRequestSchema, location=('json'))  # десериализация данных запроса
    @marshal_with(UserSchema)  # Сериализация ответа
    def post(self, **kwargs):
        user = UserModel(**kwargs)
        user.save()
        return user, 201

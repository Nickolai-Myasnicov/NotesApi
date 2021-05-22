from api import Resource, reqparse, db, abort
from api.models.user import UserModel
from api.schemas.user import UserSchema, UserRequestSchema
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs


class UserResource(MethodResource):
    @marshal_with(UserSchema)
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if not user:
            abort(404, error=f"User with id={user_id} not found")
        return user, 200

    @use_kwargs(UserRequestSchema, location=('json'))
    @marshal_with(UserSchema)
    def post(self, **kwargs):
        user = UserModel(**kwargs)
        user.save()
        return user, 201


class UsersListResource(MethodResource):
    @marshal_with(UserSchema(many=True))
    def get(self):
        users = UserModel.query.all()
        return users, 200


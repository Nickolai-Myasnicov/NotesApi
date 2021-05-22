from api import Resource, reqparse, db, abort
from api.models.user import UserModel
from api.schemas.user import user_schema, users_schema, UserSchema
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc


class UserResource(MethodResource):
    @marshal_with(UserSchema)
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if not user:
            abort(404, error=f"User with id={user_id} not found")
        return user, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        user_data = parser.parse_args()
        user = UserModel(**user_data)
        user.save()
        return user_schema.dump(user), 201


class UsersListResource(MethodResource):
    @marshal_with(UserSchema(many=True))
    def get(self):
        users = UserModel.query.all()
        return users, 200


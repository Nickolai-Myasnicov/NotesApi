from api import abort
from api.models.tag import TagModel
from api.schemas.tag import TagSchema, TagRequestSchema
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs


@doc(tags=['Tags'])
class TagResource(MethodResource):
    @marshal_with(TagSchema)
    @doc(summary="Get tag by id")
    def get(self, tag_id):
        tag = TagModel.query.get(tag_id)
        if not tag:
            abort(404, error=f"User with id={tag_id} not found")
        return tag, 200


@doc(tags=['Tags'])
class TagsListResource(MethodResource):
    @doc(summary="Get all tags")
    @marshal_with(TagSchema(many=True))
    def get(self):
        tags = TagModel.query.all()
        return tags, 200

    @doc(summary="Create new tag")
    @use_kwargs(TagRequestSchema, location=('json'))  # десериализация данных запроса
    @marshal_with(TagSchema)  # Сериализация ответа
    def post(self, **kwargs):
        tag = TagModel(**kwargs)
        tag.save()
        return tag, 201

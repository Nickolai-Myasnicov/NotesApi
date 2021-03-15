from api import ma
from api.models.tag import TagModel


# Сериализация ответа(response)
class TagSchema(ma.SQLAlchemySchema):
    class Meta:
        model = TagModel

    name = ma.auto_field()
    _links = ma.Hyperlinks({
        'self': ma.URLFor('tagresource', values=dict(tag_id="<id>")),
        'collection': ma.URLFor('tagslistresource')
    })


# Десериализация запроса(request)
class TagRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = TagModel

    name = ma.Str()

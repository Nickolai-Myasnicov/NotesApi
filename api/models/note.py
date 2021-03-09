from api import db
from api.models.user import UserModel


class NoteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey(UserModel.id))
    text = db.Column(db.String(255), unique=False, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
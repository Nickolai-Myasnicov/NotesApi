import json
from api import db
from app import app
from unittest import TestCase
from api.models.user import UserModel
from api.models.note import NoteModel
from base64 import b64encode


class TestUsers(TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_user_creation(self):
        user_data = {
            "username": 'admin',
            'password': 'admin'
        }
        res = self.client.post('/users', data=user_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertIn('admin', data.values())

    def test_users_get(self):
        users_data = [
            {
                "username": 'admin',
                'password': 'admin'
            },
            {
                "username": 'ivan',
                'password': '12345'
            },
        ]
        for user_data in users_data:
            user = UserModel(**user_data)
            user.save()

        res = self.client.get('/users')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        # print(data)
        self.assertEqual(data[0]["username"], users_data[0]["username"])
        self.assertEqual(data[1]["username"], users_data[1]["username"])

    def test_user_not_found(self):
        res = self.client.get('/users/1')
        self.assertEqual(res.status_code, 404)

    def tearDown(self):
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


class TestNotes(TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

        with self.app.app_context():
            # create all tables
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

    def test_get_note_by_id(self):
        user_data = {
            "username": 'test',
            'password': 'test'
        }

        user = UserModel(**user_data)
        user.save()
        notes_data = [
            {
                "text": 'Test note 1',
            },
            {
                "text": 'Test note 2',
            },
        ]
        ids = []
        for note_data in notes_data:
            note = NoteModel(author_id=user.id, **note_data)
            note.save()
            ids.append(note.id)

        headers = {
            'Authorization': 'Basic ' + b64encode(f"{user_data['username']}:{user_data['password']}".encode('ascii')).decode('utf-8')
        }
        res = self.client.get('/notes', headers=headers)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(len(data), 2)


        # ...
        # user_data = [{"username": "Vazgen", "password": "test"},
        #              {"username": "Mihalych", "password": "test"},
        #              {"username": "Vasilij", "password": "test"}]
        #
        # for user in user_data:
        #     self.client.post('/users', data=user)
        #
        # users = UserModel.query.all()
        # self.assertEqual(len(users), len(user_data))
        #
        # # for user in users:
        # self.assertEqual(user_data[0]["username"], users[0]["username"])

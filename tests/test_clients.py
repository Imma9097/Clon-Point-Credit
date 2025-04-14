import unittest
from app import create_app, db

class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def test_create_client(self):
        response = self.client.post('/clients', json={
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "1234567890"
        })
        self.assertEqual(response.status_code, 201)
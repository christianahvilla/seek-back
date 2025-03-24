import unittest
from flask_testing import TestCase
from app import app
from models.user import create_user
from flask_jwt_extended import decode_token

class TestAuth(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['JWT_SECRET_KEY'] = 'test-secret-key'
        return app

    def setUp(self):
        create_user("test@example.com", "Test User", "password123")

    def tearDown(self):
        pass

    def test_register_user(self):
        response = self.client.post('/register', json={
            "email": "newuser@example.com",
            "name": "New User",
            "password": "newpassword123"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json)

    def test_login_user(self):
        response = self.client.post('/login', json={
            "email": "test@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json)

        token = response.json["access_token"]
        decoded_token = decode_token(token)
        self.assertEqual(decoded_token["email"], "test@example.com")
        self.assertEqual(decoded_token["name"], "Test User")

    def test_login_invalid_credentials(self):
        response = self.client.post('/login', json={
            "email": "test@example.com",
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn("error", response.json)

if __name__ == '__main__':
    unittest.main()
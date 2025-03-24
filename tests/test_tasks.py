import unittest
from flask_testing import TestCase
from app import app
from models.task import create_task
from models.user import create_user
from flask_jwt_extended import create_access_token

class TestTasks(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['JWT_SECRET_KEY'] = 'test-secret-key'
        return app

    def setUp(self):
        create_user("test@example.com", "Test User", "password123")
        self.access_token = create_access_token(identity="test@example.com")

        create_task("test-task-id", "Test Task", "This is a test task", "todo", "test@example.com")

    def tearDown(self):
        pass

    def test_create_task(self):
        response = self.client.post('/tasks', json={
            "title": "New Task",
            "description": "This is a new task",
            "status": "todo"
        }, headers={"Authorization": f"Bearer {self.access_token}"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("task_id", response.json)

    def test_get_all_tasks(self):
        response = self.client.get('/tasks', headers={"Authorization": f"Bearer {self.access_token}"})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_single_task(self):
        response = self.client.get('/tasks/test-task-id', headers={"Authorization": f"Bearer {self.access_token}"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["id"], "test-task-id")

    def test_update_task(self):
        response = self.client.put('/tasks/test-task-id', json={
            "title": "Updated Task",
            "description": "This is an updated task",
            "status": "in_progress"
        }, headers={"Authorization": f"Bearer {self.access_token}"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["title"], "Updated Task")
        self.assertEqual(response.json["description"], "This is an updated task")
        self.assertEqual(response.json["status"], "in_progress")

    def test_delete_task(self):
        response = self.client.delete('/tasks/test-task-id', headers={"Authorization": f"Bearer {self.access_token}"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json)

if __name__ == '__main__':
    unittest.main()
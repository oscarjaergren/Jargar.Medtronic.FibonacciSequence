import unittest
from src.fibonacci_server import app


class TestFibonacciServer(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()  # Use the app from your server code
        self.app.testing = True

    def test_get_first_fibonacci_value(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')
        self.assertEqual(response.data.decode('utf-8'), '0')

    def test_get_second_fibonacci_value(self):
        self.app.get('/')
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')
        self.assertEqual(response.data.decode('utf-8'), '1')

    def test_get_third_fibonacci_value(self):
        self.app.get('/')
        self.app.get('/')
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')
        self.assertEqual(response.data.decode('utf-8'), '1')

    def test_non_get_request(self):
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

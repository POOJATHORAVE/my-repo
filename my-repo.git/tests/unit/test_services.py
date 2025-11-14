# tests/unit/test_services.py
import unittest
from app.models import User
from app.services import greet

class TestServices(unittest.TestCase):
    def test_greet_returns_string(self):
        user = User(name="Bob")
        result = greet(user)
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()

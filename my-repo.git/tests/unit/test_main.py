# tests/unit/test_main.py
import unittest
from app.models import User
from app.services import greet

class TestMain(unittest.TestCase):
    def test_greet_function(self):
        user = User(name="Alice")
        self.assertEqual(greet(user), "Hello, Alice! Welcome to the app.")

if __name__ == "__main__":
    unittest.main()

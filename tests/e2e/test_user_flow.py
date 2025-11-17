# tests/e2e/test_user_flow.py
import unittest
from app.models import User
from app.services import greet

class TestUserFlow(unittest.TestCase):
    def test_user_greeting_flow(self):
        user = User(name="Eve")
        greeting = greet(user)
        self.assertTrue("Eve" in greeting)

if __name__ == "__main__":
    unittest.main()


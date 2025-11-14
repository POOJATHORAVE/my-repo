# src/app/services.py
from app.models import User

def greet(user: User) -> str:
    return f"Hello, {user.name}! Welcome to the app."

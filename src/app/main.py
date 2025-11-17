# src/app/main.py
from app.services import greet
from app.models import User

def main():
    user = User(name="Alice")
    print(greet(user))

if __name__ == "__main__":
    main()

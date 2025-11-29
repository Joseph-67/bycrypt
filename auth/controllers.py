"""
Authentication business logic
Handles password hashing and user authentication
"""
from flask_bcrypt import Bcrypt
from models.user_model import find_user_by_email, create_user

bcrypt = Bcrypt()

def register_user(username, email, password, role="user"):
    """Register new user with hashed password"""
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    create_user(username, email, hashed_password, role)

def authenticate(email, password):
    """Authenticate user by email and password"""
    user = find_user_by_email(email)
    if user and bcrypt.check_password_hash(user['password'], password):
        return user
    return None

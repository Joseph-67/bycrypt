"""
User data access layer
All SQL queries for user operations (no ORM)
"""
from db import get_db_connection

def find_user_by_email(email):
    """Find user by email address"""
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE email=%s", (email,))
            return cur.fetchone()
    finally:
        conn.close()

def find_user_by_id(user_id):
    """Find user by ID"""
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id=%s", (user_id,))
            return cur.fetchone()
    finally:
        conn.close()

def find_user_by_username(username):
    """Find user by username"""
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE username=%s", (username,))
            return cur.fetchone()
    finally:
        conn.close()

def create_user(username, email, password_hash, role="user"):
    """Create new user with hashed password"""
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO users (username, email, password, role)
                VALUES (%s, %s, %s, %s)
            """, (username, email, password_hash, role))
            conn.commit()
    finally:
        conn.close()

def get_all_users():
    """Get all users (admin function)"""
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, username, email, role, created_at FROM users")
            return cur.fetchall()
    finally:
        conn.close()

def delete_user(user_id):
    """Delete user by ID"""
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
            conn.commit()
    finally:
        conn.close()

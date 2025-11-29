"""
Role-Based Access Control (RBAC)
Decorator for protecting routes by user role
"""
from functools import wraps
from flask import abort
from flask_login import current_user, login_required

def role_required(*roles):
    """
    Decorator to restrict access to specific roles
    Usage: @role_required('admin', 'moderator')
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def wrapper(*args, **kwargs):
            if current_user.role not in roles:
                abort(403)
            return view_func(*args, **kwargs)
        return wrapper
    return decorator

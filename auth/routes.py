"""
Authentication routes
Handles login, register, logout endpoints
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from auth.controllers import register_user, authenticate
from models.user_model import find_user_by_email, find_user_by_username

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validation
        if find_user_by_email(email):
            flash('Email already registered', 'danger')
            return redirect(url_for('auth.register'))
        
        if find_user_by_username(username):
            flash('Username already taken', 'danger')
            return redirect(url_for('auth.register'))
        
        register_user(username, email, password)
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    # Import here to avoid circular import
    from app import User
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = authenticate(email, password)
        if user:
            login_user(User(user))
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('auth.login'))

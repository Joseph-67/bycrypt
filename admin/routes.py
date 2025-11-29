"""
Admin panel routes
Protected by role_required decorator
"""
from flask import Blueprint, render_template, redirect, url_for, flash
from auth.permissions import role_required
from models.user_model import get_all_users, delete_user

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
@role_required('admin')
def admin_panel():
    """Admin dashboard - only accessible by admin role"""
    users = get_all_users()
    return render_template('admin/panel.html', users=users)

@admin_bp.route('/delete/<int:user_id>')
@role_required('admin')
def delete_user_route(user_id):
    """Delete user - admin only"""
    delete_user(user_id)
    flash('User deleted successfully', 'success')
    return redirect(url_for('admin.admin_panel'))

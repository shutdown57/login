"""Register user"""

from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_user

from src.user.model import User


register = Blueprint('register', __name__, url_prefix='/auth/register')


@register.route('/', methods=['GET', 'POST'])
def index():
    """Register user if email address is unique"""
    if request.method == 'POST':
        email = request.form.get('inputEmail')
        password = request.form.get('inputPassword')
        confirm_password = request.form.get('inputConfirm')
        if User.query.filter_by(email=email).first():
            abort(400)
        if password != confirm_password:
            abort(400)
        user = User.create({'email': email, 'password': password})
        login_user(user, False)
        return redirect(url_for('user.index'))

    return render_template('auth/register.html')

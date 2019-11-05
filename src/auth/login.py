"""Login Blueprint"""

from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_required, logout_user, login_user

from src.user.model import User


login = Blueprint('login', __name__, url_prefix='/auth/login')


@login.route('/', methods=['GET', 'POST'])
def index():
    """Sent login.html file
    if user exists and password is valid login user redirect to user index.html
    else redirect to 404 page
    """
    if request.method == 'POST':
        email = request.form['inputEmail']
        password = request.form['inputPassword']
        remember = request.form.get('inputRemember', False)
        user = User.query.filter_by(email=email).first()
        if not user or not user.verify_password(password):
            abort(404)
        login_user(user, remember=bool(remember))
        return redirect(url_for('user.index'))
    return render_template('auth/login.html')


@login.route('/logout', methods=['GET'])
def logout():
    """Logout user from session"""
    logout_user()
    return redirect(url_for('main.index'))

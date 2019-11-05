"""User route handler (user view)"""

from flask import Blueprint
from flask_login import current_user, login_required


user = Blueprint('user', __name__, url_prefix='/users')


@user.route('/', methods=['GET'])
@login_required
def index():
    """User home page"""
    return f'user {current_user.email} home page'

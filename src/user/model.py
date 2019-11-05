"""User model"""

from flask import abort
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.mixin.database import db


class User(db.Model, UserMixin):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def get_id(self) -> int:
        """Get user id"""
        return self.id

    @property
    def password(self):
        """Raise an error if someone try to get password field"""
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password_):
        """Hash password with pbdfk2 algorithm"""
        self.password_hash = generate_password_hash(password_)

    def verify_password(self, password_):
        """Verify password with user password
        return true if passwords are same
        else false
        """
        return check_password_hash(self.password_hash, password_)

    def from_dict(self, data, partial_update=True):
        """Import user data from a dictionary."""
        for field in ['email', 'password']:
            try:
                setattr(self, field, data[field])
            except KeyError:
                if not partial_update:
                    abort(400)

    @staticmethod
    def create(user_data):
        """Create a new user."""
        user = User()
        user.from_dict(user_data, partial_update=False)
        db.session.add(user)
        db.session.commit()
        return user

    def __repr__(self):
        return f'USER <{self.id}  {self.email}>'


class Anonymous(AnonymousUserMixin):
    """Guest user"""
    def __init__(self):
        self.username = 'Guest'

    def is_admin(self) -> bool:
        """A guest user can not be admin"""
        return False

    def __repr__(self) -> str:
        return f'USER <GUEST>'

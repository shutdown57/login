"""Application Factory"""

from flask import Flask
from flask_login import LoginManager

from src.user.model import User


def create_app(config_class: str) -> Flask:
    """Create app

    :param config_class: config class name
    :return: Flask instance
    """
    app = Flask(__name__)
    app.config.from_object(f'config.{config_class}')

    from src.mixin.database import db

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login.index"

    @login_manager.user_loader
    def load_user(user_id: int) -> User:
        """Loadu user with LoginManager"""
        if user_id is None:
            return
        user = User.query.filter_by(id=user_id).first()
        if user:
            return user

    from src.main import main as bp_main
    from src.auth.register import register as bp_register
    from src.auth.login import login as bp_login
    from src.user.view import user as bp_user

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_register)
    app.register_blueprint(bp_login)
    app.register_blueprint(bp_user)

    with app.app_context():
        db.create_all()

    return app

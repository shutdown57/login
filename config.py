"""Application Configuration file"""

import os


class Config:
    """Base config class"""
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_SERVER = 'localhost'
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    SQLALCHEMY_DATABASE_URI = f'postgresql://root:root@{DB_SERVER}:8080/login'

    def __repr__(self) -> str:
        return f'Base config'


class Development(Config):
    """Development config class"""
    TESTING = False
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True

    def __repr__(self):
        return f'Development config {self.DEBUG}'


CONFIG = {
    'default': Development,
    'development': Development
}

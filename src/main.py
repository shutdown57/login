"""Main route handler (main view)"""

from flask import Blueprint, render_template

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/', methods=['GET'])
def index():
    """Return index file (home page)"""
    return render_template('index.html')

from flask import Blueprint

test_bp = Blueprint('teste', __name__)

@test_bp.route('/')
def home():
    return '<h1>Hello World!</h1>'

@test_bp.route('/about')
def about():
    return '<h1>Welcome to about session!</h1>'
from flask import Flask
# Blueprints help modularize routes, resulting in better organization.
from blueprints.test_routes import test_bp
from blueprints.html_example.html_example import html_bp

app = Flask(__name__)
app.register_blueprint(test_bp) # Link app.py to blueprint routes
app.register_blueprint(html_bp)

if __name__ == "__main__":
    app.run()
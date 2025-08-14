from flask import Blueprint, render_template

# To render templates, it is necessary to provide the path in the 'template_folder' argument.
# To serve static files, do the same in the 'static_folder' argument.
# The 'static_url_path' tells Flask the path to the static files.
html_bp = Blueprint('html', __name__, template_folder='templates', static_folder='static', static_url_path='/blueprints/html_example/static')

@html_bp.route('/html')
def html():
    return render_template('index.html')
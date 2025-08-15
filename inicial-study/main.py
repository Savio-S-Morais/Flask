from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/<string:nameflask>')
def about(nameflask):
    return render_template('about.html', namehtml = nameflask)

@app.route('/<string:url>')
def error(url):
    url = escape(url) # The function 'escape' remove special character, like HTML characters use for open and close tags
    return f"Sorry, but the page <i>'{url}'</i> doesn't exit", 400

if __name__ == "__main__":
    app.run()
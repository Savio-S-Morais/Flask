from flask import Flask, render_template, request, redirect, url_for
from database import database # Import the 'database' instance from database.py
from models import Users # Import the User class that maps to the database table

app = Flask(__name__)

# Set the path for the database file and initialize the database with the app
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
database.init_app(app)

@app.route('/')
def home():
    users = database.session.query(Users).all()

    return render_template('home.html', users = users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        name = request.form['name']
        contact = request.form['contact']

        new_user = Users(name=name, contact=contact)
        database.session.add(new_user)
        database.session.commit()
    
    return redirect(url_for('home'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = database.session.query(Users).filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('update.html', user=user)
    else:
       name = request.form['name']
       contact = request.form['contact']

       user.name = name
       user.contact = contact
       database.session.commit() 
       
       return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    user = database.session.query(Users).filter_by(id=id).first()
    database.session.delete(user)
    database.session.commit()

    return redirect(url_for('home'))

if __name__ == "__main__":
    # Create the database if it doesn't exist
    with app.app_context():
        database.create_all()

    app.run()
from database import database # Import the 'database' instance from database.py

# Define classes that represent database tables for ORM mapping
class Users(database.Model):
    __tablename__ = 'Users'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(40), nullable=False)
    contact = database.Column(database.Integer, nullable=False)

    def __repr__(self):
        return f"<{self.name}>"
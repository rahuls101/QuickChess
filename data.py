from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), nullable = False)
    username = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(200), nullable = False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
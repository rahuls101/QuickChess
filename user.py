from data import db, User

def create_user(email, username, password): 
    new_user = User(email, username, password)
    db.session.add(new_user)
    db.session.commit()


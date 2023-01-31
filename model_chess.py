import os

from __init__ import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    __tablename__ = 'chess_users'

    
    # Define the Users schema
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    dob = db.Column(db.String(255), unique = False, nullable=False)
    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    # notes = db.relationship("Notes", cascade='all, delete', backref='users', lazy=True)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, uid="1", password="null", dob="11-11-1111", games=[]):
        self.uid = uid
        self.name = name
        self.dob = dob
        self.set_password(password)

    # returns a string representation of object, similar to java toString()
    def __repr__(self):
        return "Users(" + str(self.uid) + "," + self.name + "," + str(self.dob) + ")"

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "password": self.password,
            "dob": self.dob
        }

    def read2(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "dob": self.dob,
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name="", uid="", password="", dob=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(uid) > 0:
            self.uid = uid
        if len(password) > 0:
            self.set_password(password)
        if len(dob) > 0:
            self.dob = dob
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

    # set password method is used to create encrypted password
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    # check password to check versus encrypted password
    def is_password_match(self, password):
        """Check hashed password."""
        result = check_password_hash(self.password, password)
        return result

    # required for login_user, overrides id (login_user default) to implemented userID
    def get_id(self):
        return self.uid

def getUser(uid):
    users = Users.query.all()
    for user in users:
        if(user.get_id() == uid):
            user_object = user
    return user_object


if __name__ == "__main__":
    print(getUser(420).dob)
    # """Create required directories"""
    # try:
    #     os.makedirs('volumes')
    #     os.makedirs('volumes/uploads')
    # except:
    #     pass
    # """Create database and tables"""
    # db.create_all()
    # u1 = Users(name='Toby', uid='69420', password='123toby', dob="11-11-1111")
    # try:
    #     '''add user/note data to table'''
    #     db.session.add(u1)
    #     db.session.commit()
    # except IntegrityError:
    #     '''fails with bad or duplicate data'''
    #     db.session.remove()
    #     print(f"Records exist, duplicate email, or error: {u1.uid}")

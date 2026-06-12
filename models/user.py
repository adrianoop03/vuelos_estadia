from models.db import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, default=False)  # True for admin, False for user

    def __init__(self, name, email, password_hash, admin):
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.admin = admin


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'admin': self.admin
        }    
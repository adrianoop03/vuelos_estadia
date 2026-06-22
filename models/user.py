from models.db import db
from flask_login import UserMixin


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    verified = db.Column(db.Boolean, default=False)  # Verificacion del usuario
    admin = db.Column(db.Boolean, default=False)  # True para admin, False para usuario

    def __init__(self, name, email, password, verified, admin):
        self.name = name
        self.email = email
        self.password = password
        self.verified = verified
        self.admin = admin


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'verfied': self.verified,
            'admin': self.admin
        }    
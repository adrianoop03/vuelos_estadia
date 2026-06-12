from models.user import User
from models.db import db

def obtenerUsuarios():
    users = User.query.all()
    return [User.serialize() for User in users]


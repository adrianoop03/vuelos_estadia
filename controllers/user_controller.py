from models.user import User
from models.db import db
from werkzeug.security import generate_password_hash, check_password_hash
def obtenerUsuarios():
    users = User.query.all()
    return [User.serialize() for User in users]

def crearUsuario(data):
    usuarioExiste = User.query.filter_by(email=data["email"]).first()
    if usuarioExiste:
        return "Error: El usuario ya existe", 400
    usuario_nuevo = User(
    name=data["name"],
    email=data["email"],
    password=generate_password_hash(data["password"]),
    admin=data.get("admin", False))
    db.session.add(usuario_nuevo)
    db.session.commit()
    return usuario_nuevo.serialize(), 201

def iniciarSesion(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user.serialize(), 200
    else:
        return "Error: Credenciales inválidas", 401
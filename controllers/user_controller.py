from flask import Flask, current_app, render_template, request, redirect, url_for
from flask_mail import Message
from models.user import User
from models.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from extensions import mail


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
    verified = data.get("verified", False),
    admin=data.get("admin", False))
    db.session.add(usuario_nuevo)
    db.session.commit()
    return usuario_nuevo.serialize(), 201

def verificacionCorreo(email, token):
    msg = Message(
        "Verificacion de cuenta",
        
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[email]
    )

    msg.body = f"""
    Para verificar tu cuenta visita:

    http://localhost:5000/verif/{token}
    """
    mail.send(msg)

    print ("Correo enviado a", email, 200)

def verificarUsuario(email):
    user = User.query.filter_by(email=email).first()
    user.verified = True
    db.session.commit()


def iniciarSesion(email, password):
    user = User.query.filter_by(email=email).first()
    
    if user and check_password_hash(user.password, password):
        return user, 200

    return None, 401
    
def existeCorreo(email):
    email = User.query.filter_by(email=email).first()
    if not email:
        return "El correo no existe", 400
    return "Correo existente...", 200
    
def correo_recuperacion(email, token):
    msg = Message(
        "Recuperacion de contrasena",
        
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[email]
    )

    msg.body = f"""
    Para recuperar tu contrasena visita:

    http://localhost:5000/reset/{token}
    """
    mail.send(msg)

    return "Correo enviado", 200

def cambiarContrasena(email, nueva_contrasena):
    user = User.query.filter_by(email=email).first()
    if user:
        user.password = generate_password_hash(nueva_contrasena)
        db.session.commit()
        return "Contraseña actualizada", 200
    else:
        return "Error: Usuario no encontrado", 404
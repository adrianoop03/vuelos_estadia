from flask import Blueprint, app, jsonify, redirect, render_template, request
from itsdangerous import URLSafeTimedSerializer
from models.db import db
from models.user import User
from controllers.user_controller import *


user = Blueprint('user', __name__)

@user.route('/users', methods=['GET'])
def get_users():
    users = obtenerUsuarios()
    return jsonify(users)

@user.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user, status_code = crearUsuario(data)
    return jsonify(user), status_code



@user.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@user.route('/login', methods=['POST'])
def login_user():

    email = request.form.get('email')
    password = request.form.get('password')

    user, status_code = iniciarSesion(email, password)

    if status_code == 200:
        return redirect('/users')
    

    return render_template(
        'login.html',
        error='Correo o contraseña incorrectos'
    )
    
#Correo de recuperacion de contraseña
@user.route('/reset-password' , methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data.get('email')
    serializer = URLSafeTimedSerializer("clave_secreta")
    token = serializer.dumps(email)
    message, status_code = correo_recuperacion(email, token)
    return jsonify(message), status_code

#Cambio de contraseña
@user.route('/reset/<token>')
def change_password(token):

    serializer = URLSafeTimedSerializer("clave_secreta")

    try:
        email = serializer.loads(token, max_age=3600)
        return f"Token válido para: {email}"

    except Exception:
        return "Token inválido o expirado"
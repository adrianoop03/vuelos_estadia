from flask import Blueprint, app, jsonify, redirect, render_template, request
from itsdangerous import URLSafeTimedSerializer
from models.db import db
from models.user import User
from controllers.user_controller import *


user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = obtenerUsuarios()
    return jsonify(users)

@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    serializer = URLSafeTimedSerializer("clave_secreta")
    token = serializer.dumps(email, salt="verif_mail")
    user, status_code = crearUsuario(data)
    verificacionCorreo(email, token)
    return jsonify(user), status_code

@user_bp.route('/verif/<token>')
def verif_mail(token):

    serializer = URLSafeTimedSerializer("clave_secreta")

    try:
        email = serializer.loads(token, max_age=3600, salt="verif_mail")
        verificarUsuario(email)
        return f"Token válido para: {email}"
    
    except Exception:
        return "Token inválido o expirado"   

@user_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@user_bp.route('/login', methods=['POST'])
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
@user_bp.route('/reset-password' , methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data.get('email')
    serializer = URLSafeTimedSerializer("clave_secreta")
    token = serializer.dumps(email, salt="change_pass")
    message, status_code = correo_recuperacion(email, token)
    return jsonify(message), status_code

#Cambio de contraseña
@user_bp.route('/reset/<token>', methods=["GET", "POST"])
def change_password(token):

    serializer = URLSafeTimedSerializer("clave_secreta")

    try:
        email = serializer.loads(token, max_age=3600, salt="change_pass")
        
    except Exception:
        return "Token inválido o expirado"
    
    if request.method == "GET":
        return render_template(
            "reset_password.html",
            token=token
        )
    data = request.get_json()
    password = data.get("password")

    if not password:
        return "La contraseña es obligatoria", 400

    cambiarContrasena(email, password)

    return "Contraseña actualizada correctamente"
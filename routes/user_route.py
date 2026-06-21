from flask import Blueprint, jsonify, redirect, render_template, request, flash, url_for
from itsdangerous import URLSafeTimedSerializer
from models.db import db
from models.user import User
from controllers.user_controller import *
from flask_login import login_user, login_required, logout_user, current_user
from controllers.team_controller import get_all_teams
from controllers.stays_controller import get_all_stay
from controllers.stadium_controller import get_all_stadiums

user_bp = Blueprint('user', __name__)

"""@user_bp.route('/users', methods=['GET'])
@login_required
def get_users():
    users = obtenerUsuarios()
    return jsonify(users)"""

@user_bp.route('/register', methods=['GET'])
def register_hud():
    return render_template("register.html")

@user_bp.route('/register', methods=['POST'])
def register_user():

    data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "password": request.form.get("password")
    }
    #Confirmar contraseña
    confirm_password = request.form.get("confirm_password")

    if data["password"] != confirm_password:
        return render_template(
            "register.html",
            error="Las contraseñas no coinciden."
        )

    email = data["email"]

    serializer = URLSafeTimedSerializer("clave_secreta")
    token = serializer.dumps(email, salt="verif_mail")

    user, status_code = crearUsuario(data)

    if status_code != 201:
        return render_template(
            "register.html",
            error=user
        )

    verificacionCorreo(email, token)

    flash(
        "Te enviamos un correo de verificación. Revisa tu bandeja de entrada.",
        "success"
    )

    return redirect(url_for("user.login_page"))

@user_bp.route('/verif/<token>')
def verif_mail(token):

    serializer = URLSafeTimedSerializer("clave_secreta")

    try:
        email = serializer.loads(token, max_age=3600, salt="verif_mail")
        verificarUsuario(email)
        return f"Token válido para: {email}"
    
    except Exception:
        return "Token inválido o expirado"   

#Sistema de login

@user_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@user_bp.route('/login', methods=['POST'])
def login_user_route():

    email = request.form.get('email')
    password = request.form.get('password')
    remember = request.form.get('remember') == 'on'

    user, status_code = iniciarSesion(email, password)

    if status_code == 200:
        if not user.verified:
            flash('Correo no verificado.', 'danger')
            return render_template(
                'login.html'
            )
        login_user(user, remember=remember)
        
        if current_user.admin:
            return redirect(url_for('user.adminVista'))
        
        return redirect(url_for('user.usersVista'))

    flash('Correo o contraseña incorrectos.', 'danger')
    return render_template("login.html")
 
@user_bp.route('/index', methods=['GET'])
def user_index():
    return render_template("index.html")

@user_bp.route("/admin")
def adminVista():
    if current_user.admin:
        teams = get_all_teams()
        stays = get_all_stay()
        stadiums = get_all_stadiums()
        return render_template("admin.html", teams=teams, stays=stays, stadiums=stadiums)
    return "Tienes que ser admin", 400

@user_bp.route("/users")
def usersVista():
    if current_user.id:
        return render_template("users.html")
    return "Tienes que estar registrado", 400
    
    

@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.user_index'))

    
#Correo de recuperacion de contraseña

@user_bp.route('/reset-password' , methods=['GET'])
def reset_password_hud():
    return render_template("forgot_password.html")

@user_bp.route('/reset-password' , methods=['POST'])
def reset_password():
    email = request.form.get('email')
    message, verif = existeCorreo(email)
    if verif == 200:
        serializer = URLSafeTimedSerializer("clave_secreta")
        token = serializer.dumps(email, salt="change_pass")
        message, status_code = correo_recuperacion(email, token)
        return jsonify(message), status_code
    return jsonify(message), verif

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
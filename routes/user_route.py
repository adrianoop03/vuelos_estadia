from flask import Blueprint, jsonify, redirect, render_template, request
from models.db import db
from models.user import User
from controllers.user_controller import iniciarSesion, obtenerUsuarios, crearUsuario
from flask import render_template

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
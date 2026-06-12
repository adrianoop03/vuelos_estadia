from flask import Blueprint, jsonify, request
from models.db import db
from models.user import User
from controllers.user_controller import iniciarSesion, obtenerUsuarios, crearUsuario

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

@user.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user, status_code = iniciarSesion(email, password)
    return jsonify(user), status_code
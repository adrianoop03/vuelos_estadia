from flask import Blueprint, jsonify, request
from models.db import db
from models.user import User
from controllers.user_controller import obtenerUsuarios

user = Blueprint('user', __name__)

@user.route('/users', methods=['GET'])
def get_users():
    users = obtenerUsuarios()
    return jsonify(users)


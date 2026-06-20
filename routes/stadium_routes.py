from flask import Blueprint, jsonify, request
from models.stadium import Stadium
from controllers.stadium_controller import *

stadium_bp = Blueprint('stadium_bp', __name__)

@stadium_bp.route('/stadiums', methods=['GET'])
def listar_estadios():
    return jsonify(get_all_stadiums())

@stadium_bp.route('/stadiums/<int:id_stadium>', methods=['GET'])
def obtener_estadio(id_stadium):
    stadium = get_stadium_by_id(id_stadium)
    if stadium:
        return jsonify(stadium)
    else:
        return jsonify({'message': 'Estadio no encontrado'}), 404
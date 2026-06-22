from flask import Blueprint, jsonify, request
from controllers.stays_controller import (
    get_all_stay,
    get_stay_by_id,
    create_stay,
    update_stay,
    borrar_stay
)

stays_bp = Blueprint('stays_bp', __name__)


# GET /stays → lista todas las estadías
@stays_bp.route('/stays', methods=['GET'])
def listar_stays():
    return jsonify(get_all_stay())


# GET /stays/<id> → una estadía por id
@stays_bp.route('/stays/<int:id_stay>', methods=['GET'])
def obtener_stay(id_stay):
    stay = get_stay_by_id(id_stay)
    if stay:
        return jsonify(stay)
    return jsonify({'message': 'Estadía no encontrada'}), 404


# POST /stays → crear nueva estadía
@stays_bp.route('/stays', methods=['POST'])
def crear_stay():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Datos inválidos'}), 400

    required = ['team', 'name_stays', 'pais', 'estado', 'ciudad']
    missing = [f for f in required if not data.get(f)]
    if missing:
        return jsonify({'message': f'Campos requeridos: {", ".join(missing)}'}), 400

    nueva = create_stay(
        team=data['team'],
        name_stays=data['name_stays'],
        pais=data['pais'],
        estado=data['estado'],
        ciudad=data['ciudad']
    )
    return jsonify(nueva), 201


# PUT /stays/<id> → actualizar estadía
@stays_bp.route('/stays/<int:id_stay>', methods=['PUT'])
def actualizar_stay(id_stay):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Datos inválidos'}), 400

    actualizada = update_stay(
        id=id_stay,
        team=data.get('team'),
        name_stays=data.get('name_stays'),
        pais=data.get('pais'),
        estado=data.get('estado'),
        ciudad=data.get('ciudad')
    )
    if actualizada:
        return jsonify(actualizada)
    return jsonify({'message': 'Estadía no encontrada'}), 404


# DELETE /stays/<id> → eliminar estadía
@stays_bp.route('/stays/<int:id_stay>', methods=['DELETE'])
def eliminar_stay(id_stay):
    ok = borrar_stay(id_stay)
    if ok:
        return jsonify({'message': 'Estadía eliminada correctamente'})
    return jsonify({'message': 'No se pudo eliminar la estadía'}), 404
from flask import blueprints, jsonify, request
from TeamTransit.models import Stadium
from TeamTransit.controllers import stadium_controller

@stadium_controller.route('/stadiums', methods=['GET'])
def listar_productos():
    return jsonify(stadium_controller.get_all_stadiums())

@stadium_controller.route('/stadiums/<int:id_stadium>', methods=['GET'])
def obtener_producto(id_stadium):
    stadium = stadium_controller.get_stadium_by_id(id_stadium)
    if stadium:
        return jsonify(stadium)
    else:
        return jsonify({'message': 'Estadio no encontrado'}), 404
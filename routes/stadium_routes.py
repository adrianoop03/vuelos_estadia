from flask import blueprints, jsonify, request
from TeamTransit.models import Stadium
from TeamTransit.controllers import stadium_controller

@stadium_controller.route('/stadiums', methods=['GET'])
def listar_productos():
    return jsonify(stadium_controller.get_all_stadiums())
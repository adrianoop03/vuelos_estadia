from flask import blueprints, jsonify, request
from TeamTransit.models import team
from TeamTransit.controllers import team_controller

@team_controller.route('/teams', methods=['GET'])
def listar_equipos():
    return jsonify(team_controller.get_all_teams())

@team_controller.route('/teams/<int:id_team>', methods=['GET'])
def obtener_equipo_por_id(id_team):
    equipo = team_controller.get_team_by_id(id_team)
    if equipo:
        return jsonify(equipo)
    else:
        return jsonify({'message': 'Equipo no encontrado'}), 404